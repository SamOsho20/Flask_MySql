from flask_app import app
from flask import render_template, redirect, request, session, flash
#to use flash directly in this file we must import it like line 3
from flask_app.models.user  import User
from flask_app.models.show  import Show
from flask_app.models.comment import Comment
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)




#route to take us to page to create a show
@app.route('/create_show')
def create_show():
    return render_template('create_show.html')


#route to process the data for new show and redirect to dashboard
@app.route('/process_show', methods = ['post'])
def creating_show():
    
    if 'user_id' not in session :
        return redirect('/')
    if Show.validate_show(request.form):
        data={

            'title': request.form['title'],
            'network': request.form['network'],
            'release_date': request.form['release_date'],
            'comments': request.form['comments'],
            'user_id': session['user_id']
        }
        Show.create_show(data)
        # this_date = Show.format_date({'id': 'show_id'})
        return redirect('/dashboard')
    return redirect ("/create_show")

# App route to delete show
@app.route('/delete/<int:show_id>')
def delete_show(show_id):
    Show.delete_show({'id': show_id})
    return redirect ('/dashboard')


#app route to render template to show edit page 
@app.route('/edit/<int:show_id>')
def edit_show(show_id):
    if 'user_id' not in session :
        return redirect('/')
    show_info = Show.get_one_show({'id': show_id})
    return render_template('/edit_show.html', show_info = show_info)



# app route to process show edits and redirect to dashboard
@app.route('/process_edit/<int:show_id>', methods = ['post'])
def process_edits(show_id):

    if 'user_id' not in session :
        return redirect('/')
    if Show.validate_show_edit(request.form):
        data = {
                'title': request.form['title'],
                'network': request.form['network'],
                'release_date': request.form['release_date'],
                'comments': request.form['comments'],
                'show_id': show_id
                }
        Show.edit_show(data)
        return redirect('/dashboard')
    return redirect(f'/edit/{show_id}')

#route to render template that shows the display all page
@app.route('/display_show/<int:show_id>')
def get_show_with_id(show_id):
    if 'user_id' not in session :
        return redirect('/')
    data = {'id' : show_id}
    this_show = Show.get_show_from_this_user(data)
    all_comments = Comment.show_this_shows_comment({'id': show_id})
    return render_template('/display_show.html',this_show = this_show,all_comments = all_comments)

@app.route('/process_comment/<int:show_id>')
def process_comment(show_id):
    if 'user_id' not in session :
        return redirect('/')
    data = {
        'comment': request.form['comment'],
        'show_id': show_id,
        'user_id': session['user_id']
    }
    Comment.create_comment(data)
    return render_template (f'/display_show/{show_id}')
    


# @app.route('/process_my_pie/<int:pie_id>', methods = ['POST'])
# def editing_pie(pie_id):
#         if 'user_id' not in session:
#             return redirect ('/')
#         if Pie.validate_updated_pie(request.form):
#             data = {
#                 'name': request.form['name'],
#                 'ingredients': request.form['ingredients'],
#                 'size': request.form['size'],
#                 'id': pie_id
#                 }
#             Pie.update_pie(data)
#             return redirect('/dashboard')
#         return redirect(f"/edit/{pie_id}")
