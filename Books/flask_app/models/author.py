from flask_app.config.mysqlconnection import connectToMySQL
class Author:
    DB = "booksandauthors_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data ["created_at"]
        self.updated_at = data['updated_at']


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

    
