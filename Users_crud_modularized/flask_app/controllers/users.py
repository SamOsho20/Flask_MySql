from flask_app import app
from flask import request, redirect, session, render_template 
from flask_app.models.user import User 
# connecting models file and the class



@app.route('/')
def show_users():
    list_users = User.get_all_users()
    return render_template('read.html', all_users = list_users)

@app.route('/process', methods = ['POST'])
# here we connect our process form, and give it data to process and store 
def create_user():
    data ={
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'],
    }
    if request.form['first_name'] =='' and request.form['last_name'] =='' and  request.form['first_name'] =='':
        return redirect('/')
    #if the user inputs a blank info the page will redirect to teh home page, and not add in a new user with blank info!!
    User.save(data)

    # we then redirect back to our home page
    return redirect('/')


@app.route('/create_user')
def create_user_users2():
    # the save method in the user.py file requires an argument for data, 
    # so we give it request.form here bc we it has everything in data
    return render_template('create.html')


@app.route('/show_user<int:user_id>')
#we must enter in user id to keep track of the user clicked
def show_user(user_id):
    this_user = User.get_one(user_id)

    return render_template('show.html', this_user = this_user)


@app.route('/updating_user<int:user_id>', methods = ['post'])
def updating_user(user_id):
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        'user_id': user_id
        # #since we are tracking the user we  can just set it to whatever the id is without 
        # saying request.from, this way 
        # the database knows who to update 
    }
    User.updating_user(data)
    # #here we connect out classmethods with 
    # the appropriate name and function that will go in and update a user

    return redirect('/')


@app.route('/update_user<int:user_id>')
def update_user(user_id):
    this_user = User.get_one(user_id)
    return render_template('edit.html', this_user = this_user)
# @app.route('/update_user')
# def update_user():
    

#     return render_template('show.html', this_user = this_user)

@app.route('/delete_user<int:user_id>')
def delete_user(user_id):
    User.delete_user(user_id)
    return redirect('/')
