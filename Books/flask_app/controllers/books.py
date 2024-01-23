from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.book import Book
from flask_app.models.author import Author

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


@app.route('/all_books')
def get_all_books():
    all_books = Book.get_all_books()
    return render_template('/all_books.html', all_books = all_books)

@app.route('/add_new_book', methods = ['post'])
def add_new_book():
    data = {
        'title': request.form['title'],
        'pages': request.form['num_of_pages']
    }
    Book.add_new_book(data)
    return redirect('/all_books')

@app.route('/show_book/<int:book_id>')
def get_one_books(book_id):
    one_book = Book.get_one_book({'id': book_id})
    author_is = Book.get_books_with_authors({'id': book_id})
    all_authors = Author.get_all_authors()
    return render_template('/show_book.html', one_book = one_book, author_is = author_is, all_authors = all_authors)


@app.route('/add_books_favoriters', methods = ['post'])
def add_books_favoriters():
    data= {
        'book_id': request.form['book_id'],
        'author_id' : request.form['author_id']
        # we will use a hidden input to send us the author_id

    }
    Author.add_favorite_book(data)
    return redirect(f"/show_book/{data['book_id']}")


# for post form we need 2/3 routes 
#  - a route that takes us to the page 
#  - a route that processes teh page 
#  - and a a route that we can redirect to after the processing is done 

