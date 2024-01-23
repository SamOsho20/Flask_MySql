from flask import Flask, request, redirect, session, render_template, flash
from user import User

app = Flask(__name__)

@app.route('/')
def show_users():
    list_users = User.get_all_users()
    return render_template('read.html', all_users = list_users)

@app.route('/process', methods = ['POST'])
# here we connect our process form, and give it dat to process and store 
def create_user():
    if User.validate_user(request.form):
        #so after line 15 our server goes to our user.py file into the 
        # method validate_user to find the function 
        # if the function is true we will go forward and execute lines 21 - 29
        # save the data and  display it on the home page 
        #however if the line 15 is false it will skip down 
        # to line 29 and give the user a retry to enter a new user 

        data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        }
        User.save(data)
    # we then redirect back to our home page
        return redirect('/')
    
    return redirect ('/create_user')
    



@app.route('/create_user')
def create_user_users2():
    # the save method in the user.py file requires an argument for data, 
    # so we give it request.form here bc we it has everything in data
    return render_template('create.html')


if __name__ == "__main__":
    app.secret_key = "shhhhhh"
    app.run(debug=True)

