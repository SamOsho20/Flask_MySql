from flask_app import app
from flask import render_template, redirect, request, session, flash
#to use flash directly in this file we must import it like line 3
from flask_app.models.user  import User
from flask_app.models.pie  import Pie
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route('/process_pie', methods = ['POST'])
def new_pie():
    if 'user_id' not in session:
        return redirect ('/')
    data={
            'user_id': session['user_id'],
            'name': request.form['name'],
            'ingredients': request.form['ingredients'],
            'size': request.form['size']
    }
    Pie.create_new_pie(data)

    return redirect('/dashboard')



@app.route('/delete/<int:pie_id>')
def delete_pie(pie_id):
    Pie.delete_pie(pie_id)
    return redirect('/dashboard')



@app.route('/edit/<int:pie_id>')
def edit_pie(pie_id):
    if 'user_id' not in session:
        return redirect ('/')
    this_pie = Pie.get_one_pie({'id': pie_id})
    return render_template('/edit_pie.html', this_pie = this_pie)

@app.route('/process_my_pie/<int:pie_id>', methods = ['POST'])
def editing_pie(pie_id):
        if 'user_id' not in session:
            return redirect ('/')
        if Pie.validate_updated_pie(request.form):
            data = {
                'name': request.form['name'],
                'ingredients': request.form['ingredients'],
                'size': request.form['size'],
                'id': pie_id
                }
            Pie.update_pie(data)
            return redirect('/dashboard')
        return redirect(f"/edit/{pie_id}")


@app.route('/show_all_pies')
def show_all_pies():
    if 'user_id' not in session:
        return redirect ('/')
    all_pies = Pie.get_all_pies_and_users()
    return render_template('/show_all_pies.html', all_pies = all_pies)


@app.route('/show_pie/<int:pie_id>')
def show_one_pie(pie_id):
    data = {'id' : pie_id}
    show_this_pie = Pie.get_one_pie(data)

    return render_template('show_one_pie.html',  show_this_pie =  show_this_pie )
    #no forward slashes before file names for render templates


                        