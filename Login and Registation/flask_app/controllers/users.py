from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user  import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route('/')
def show_loginandreg():
    return render_template('index.html')


@app.route('/register_user', methods = ['POST'])
def process_reg():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    if User.validate_registration(request.form):
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password': pw_hash
            #confrim password should not be added as column as database
            }
        User.create_user(data)
        #save the data t a method
        user_id = User.create_user(data)

        session['user_id'] = user_id
        #we are bassically saying whoever is logged in, 
        # that is  the id of the persons info that will be displayed on 
        #see  dashboard route to see how user_id gets forwarded

        return redirect (f"/dashboard/{session['user_id']}")
    if not pw_hash:
        return redirect ('/')

    return redirect('/')

#is this app route  we will display the  user ins sessions name with a oppurtunity to also logout 

@app.route('/dashboard/<int:user_id>')
def show_user(user_id):
    if session['user_id']:
        current_user = User.get_one_user({'user_id': session['user_id']})
        return render_template ('dashboard.html', current_user = current_user)
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')

@app.route('/login', methods = ['POST'])
def login():
    return redirect ('/')

    #  'bool' object is not subscriptable error 
    # return cls(results[0])