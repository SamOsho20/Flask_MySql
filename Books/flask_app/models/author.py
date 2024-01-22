from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
class Author:
    DB = "booksandauthors_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data ["created_at"]
        self.updated_at = data['updated_at']
        self.our_author = []
        self.this_book= []
        #make sure to not add commas at teh end of each instance like this 
            #self.id = data['id'],
            #self.name = data ['name'],

        #QUERY TO DISPLAY ALL AUTHORS 

    @classmethod
    def get_all_authors(cls):
        query  =  "SELECT *  from authors;"
        results = connectToMySQL(cls.DB).query_db(query)
        author_info = []
        # print(results)
        #why wont my print statement print into the terminal; when i have them here?
        for authors_info in results:
            author_info.append(cls(authors_info))
            #sorting through objects and parsing it 
        return author_info
    
    @classmethod
    def add_new_author(cls,data):
        query = 'INSERT INTO authors (name, created_at, updated_at) values (%(name)s, NOW(),NOW());'
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_authors_with_books(cls,data):
        query = """SELECT * FROM authors
                    join favorites on authors.id = favorites.author_id
                    join books on books.id = favorites.book_id
                    where authors.id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        author = cls(results[0])
        for row_from_db in results:
            book_data = {
                'id' : row_from_db['books.id'],
                'title': row_from_db['title'],
                'pages' : row_from_db['pages'],
                'created_at': row_from_db['books.created_at'],
                'updated_at' : row_from_db ['books.updated_at']
            }
            author.this_book.append(book.Book(book_data))
            # here we are saying the that in our the result from author line 41
            # , we will go into the empty list and add all this info
            # but make sure this info matches up to our BOOk class and the atributes we stored there!
        
        return author


    @classmethod
    def get_one_author(cls,data):
        query  =  """SELECT *  from authors
                    WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        author_is = cls(results[0])
        # return cls(results[0])
        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            print(row_from_db)
            author_data = {
                "id": row_from_db["id"],
                #your table name needs to be put in front of any column names that are in both tables  
                # bc you have 2 id columns in both tables you need to specify 
                # what tables id you want so the db dosent get confused
                "name": row_from_db["name"],

                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }

            author_is.our_author.append(author_data)
        
        return author_is

    

