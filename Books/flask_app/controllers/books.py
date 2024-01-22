from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.book import Book

@app.route('/add_authors_fav', methods = ['post'])
def add_new_favorites():
    data= {
        'book_id': request.form['book_id'],
        'author_id' : request.form['author_id']
        # we will use a hidden input to send us the author_id

    }
    Book.add_new_favorite(data)
    return redirect(f"/show_author/{data['author_id']}")
    # # this is how we redirect back to the page that shows 
    # the new favorites added by the author and existing favorites


# when submitting form you need at least 2/3 routes 

#  - get route to render the form 
# - post route to submit post info
# - get route to redirect to after form is submitted 