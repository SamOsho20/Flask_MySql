from flask import Flask, request, redirect, session, render_template 

from user import User

app = Flask(__name__)

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


@app.route('/updating_user', methods = ['post'])
def updating_user():
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    User.update(data)

    return redirect('/')


@app.route('/update_user<int:user_id>')
def update_user(user_id):
    this_user = User.get_one(user_id)
    return render_template('edit.html', this_user = this_user)
# @app.route('/update_user')
# def update_user():
    

#     return render_template('show.html', this_user = this_user)

if __name__ == "__main__":
    app.run(debug=True)

