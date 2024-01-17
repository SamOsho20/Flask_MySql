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

@app.route('/show_dojo/<int:dojos_id>')
def show_dojo(dojos_id):
    this_dojo = Dojo.get_dojos_with_ninjas({"id":dojos_id})
    return render_template('show_dojo.html', dojo_info = this_dojo)
    # the key value pair "id" is what is being stored on line 34 in dojo.py







