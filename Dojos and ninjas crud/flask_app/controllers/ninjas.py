from flask_app import app
from flask import request, redirect, session, render_template 
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/addninja')
def add_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('addninja.html', all_dojos = all_dojos)

@app.route('/add_ninja', methods = ['POST'])
def adding_ninja():
    Ninja.save(request.form)
    #since were only saving  the information and not changing it we just need to insert a request.form
    # instead of a list of variables that we could store and manipulate
    return redirect('/')