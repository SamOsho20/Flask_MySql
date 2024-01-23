from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
#import files not classes here!!
class Book:
    DB = "booksandauthors_schema"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.pages = data['pages']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.this_author = []

    @classmethod
    def get_books_with_authors(cls,data):
        query = """SELECT * FROM books
                    left join favorites on books.id = favorites.book_id
                    left join authors on authors.id = favorites.author_id
                    where books.id =%(id)s"""
                    # the left join here will give us a value of none when we render the template, 
                    # rather than a n arror saying taht nothing is in the index of 0 tuplex
        results = connectToMySQL(cls.DB).query_db(query,data)
        book_is = cls(results[0])
        for row_from_db in results:
            author_data = {
                'id' : row_from_db['authors.id'],
                'name': row_from_db['name'],
                'created_at': row_from_db['authors.created_at'],
                'updated_at' : row_from_db ['authors.updated_at']
            }
            #theres only one name column in both tables so no need to specify 
            # which table  query should pull name  from
            book_is.this_author.append(author.Author(author_data))

        return book_is
    
    @classmethod
    def get_all_books(cls):
        query  =  "SELECT * from books;"
        results = connectToMySQL(cls.DB).query_db(query)
        book_info = []
        # print(results)
        #why wont my print statement print into the terminal; when i have them here?
        for books_info in results:
            book_info.append(cls(books_info))
            #sorting through objects and parsing it 
        return book_info
    
    @classmethod
    def get_one_book(cls, book_id):
        query  =  "SELECT * from books where id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,book_id)
        return cls(results[0])
    @classmethod
    def add_new_favorite(cls,data):
        query  =  "INSERT INTO favorites (book_id,author_id) values (%(book_id)s, %(author_id)s);"
        #make sure to add add last parentheses at the end then semicolon and last quotations
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def add_new_book(cls,data):
        query  =  "INSERT INTO books (title,pages) values (%(title)s, %(pages)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
