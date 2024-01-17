from flask_app import app
from flask import request, redirect, session, render_template 
from flask_app.models.dojo import Dojo


@app.route('/addninja')
def add_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('addninja.html', all_dojos = all_dojos)

@app.route('/add_ninja', methods = ['POST'])
def adding_ninja():
    print(request.form)
    return redirect('/')