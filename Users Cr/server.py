from flask import Flask, request, redirect, session, render_template 

from user import User

app = Flask(__name__)

@app.route('/')
def show_users():
    list_users = User.get_all_users()
    return render_template('read.html', all_users = list_users)

@app.route('/process', methods = ['POST'])
# here we connect our process form, and give it dat to process and store 
def create_user():
    data ={
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'],
    }
    User.save(data)
    # we then redirect back to our home page
    return redirect('/')


@app.route('/create_user')
def create_user_users2():
    # the save method in the user.py file requires an argument for data, 
    # so we give it request.form here bc we it has everything in data
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)

