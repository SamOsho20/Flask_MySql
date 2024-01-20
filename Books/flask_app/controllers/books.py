from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.author import Author

@app.route('/')
def index():
    author_information = Author.get_all_authors()
    print(author_information)
    return render_template('index.html', author_information = author_information)

@app.route('/add_author', methods = ['post'])
def add_new_author():
    data={
        'name': request.form['name']
    }
    Author.add_new_author(data)
    return redirect ('/')
    # we need to create an insert statement in our query that will create a new author
