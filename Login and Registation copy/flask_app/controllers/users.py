from flask_app import app
from flask import render_template, redirect, request, session, flash
#to use flash directly in this file we must import it like line 3
from flask_app.models.user  import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route('/')
def show_loginandreg():

    return render_template('index.html')


@app.route('/register_user', methods = ['POST'])
def process_reg(): 
    if User.validate_registration(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        if pw_hash == 0:
            flash('Invalid Credentials')
            return redirect ('/')
        # user_in_db = User.get_by_email({'user_email': request.form['email']})
        # # if user_in_db:
        # #     flash('email already exists', 'reg_flash')
        # #     return redirect ('/')
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'age': request.form ['age'],
            'password': pw_hash
            #confirm password should not be added as column as database
            }
        
        # User.create_user(data)
        # if we dont comment  line 33 out it will run the query 2x!!
        #save the data to a method
        user_id = User.create_user(data)


        session['user_id'] = user_id
        #we are bassically saying whoever is logged in, 
        # that is  the id of the persons info that will be displayed on 
        #see  dashboard route to see how user_id gets forwarded

        return redirect ("/dashboard")

    return redirect('/')

#is this app route  we will display the  user ins sessions name with a oppurtunity to also logout 

@app.route('/dashboard')
def show_user():
    if 'user_id' not in session:
        return redirect ('/')
    current_user = User.get_one_user({'user_id': session['user_id']})
    return render_template ('dashboard.html', current_user = current_user)
    #!!!! line 48 is very important!! so line 45 says if a user is not in  session 
    # basically  if we have a user not logged in show him the login and reg BUT if a user is  in session/logged in
    #  send him to the dashboard . This allows
    #users not logged in should not be able to use our app so this sequence should be added on any crud methods using session
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')

@app.route('/login', methods = ['POST'])
def login():
    user_in_db = User.get_by_email({'user_email': request.form['login_email']})
    if user_in_db:
        #if line 62 this is true it will go through all the way to line 65
        if  bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            session ['user_id'] = user_in_db.id
            return redirect ("/dashboard")
    #if false line 67 and 68 will be executed 
    flash('invalid credentials', 'login')
    return redirect ('/')

    #  'bool' object is not subscriptable error 
    # return cls(results[0])