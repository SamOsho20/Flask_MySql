from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    def __init__(self,data):
        self.id = data['id'],
        self.title = data['title'],
        self.pages = data['pages']
        self.created_at = data ['created_at'],
        self.updated_at = data ['updated_at'],
        self.this_author = []

    @classmethod
    def get_books_with_authors(cls,data):
        query = """SELECT * from books 
                    join favorites on favorites.book_id = books.id
                    join books on favorites.author_id = authors.id 
                    Where books.id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        book_is = cls(results[0])
        for row_from_db in results:
            author_data = {
                'id' : row_from_db["authors.id"],
                'name': row_from_db['name'],
                'created_at': row_from_db['authors.created_at'],
                'updated_at' : row_from_db ['authors.updated_at']
            }
            book_is.this_author.append(author.Author(author_data))

            return book_is