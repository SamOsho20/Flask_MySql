from flask_app import app
from flask import request, redirect, session, render_template 
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def show_home():
    all_dojos = Dojo.get_all_dojos()
    return render_template('displayall.html', all_dojos = all_dojos)


@app.route('/process_dojo',methods = ['POST'])
def process_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)

    return redirect('/')

@app.route('/addninja')
def add_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('addninja.html', all_dojos = all_dojos)

@app.route('/add_ninja', methods = ['POST'])
def adding_ninja():
    return redirect('/')



