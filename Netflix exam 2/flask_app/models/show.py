from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import comment
import re


class Show:
    DB = 'netflix_schema'
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.comments = data['comments']
        self.creator = None


    # read to show all the shows in database 
    @classmethod
    def get_all_shows(cls):
        query = """SELECT * FROM shows;"""
        row_db = connectToMySQL(cls.DB).query_db(query)
        #this returns us backa n object of all the shows
        shows =[]
        # creating a list to put shows in bc we cant access it just as an object 

        for show in row_db:
        # for each item in our rows 
            shows.append(cls(show))
            #lets append it meaning append the values to the key values 
        
        print(shows)
        return shows
        #now lets return all that info into a list so that we can access it in our html with . notation
        #why would it print an object when i ask it to print shows on line 32????
    
    # method to create a show 
    @classmethod
    def create_show(cls,data):
        query = """INSERT INTO shows (title,network,release_date,comments,user_id)
                    VALUES( %(title)s,%(network)s,%(release_date)s,%(comments)s,%(user_id)s);"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    # method to change date format
    @classmethod
    def format_date(cls,show_id):
        query =  """SELECT DATE_FORMAT(release_date, '%M, %e, %Y') 
                    FROM shows
                    where shows.id = %(show_id)s;""" 
        results = connectToMySQL(cls.DB).query_db(query,show_id)
        return results
    #i know im on teh right track here to get teh date format to show month,
    #  day then year but i just dont know ho to connect it to my controllers file

    # Delete a show method
    @classmethod
    def delete_show(cls,data):
        query= """DELETE  FROM shows 
                    WHERE id = %(id)s """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    #method to get individual values in a specific show by its id


    # edit a show method
    @classmethod
    def edit_show(cls,data):
        query= """      UPDATE SHOWS
                        SET title = %(title)s,
                        network = %(network)s,
                        release_date = %(release_date)s,
                        comments = %(comments)s
                        WHERE id = %(show_id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    #method to get show  by id
    @classmethod
    def get_one_show(cls,data):
        query = """SELECT * FROM SHOWS 
                    WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])
    
    #method to join all shows info to the user that recommended that show
    @classmethod
    def get_show_from_this_user(cls,id):
        query = """SELECT *    
                    FROM shows 
                    JOIN users ON shows.user_id = users.id
                    Where shows.id = %(id)s;
                    """
                    #make sure names match up for id like above on lines 29,31, "user_id"
        results = connectToMySQL(cls.DB).query_db(query,id)
        this_show = cls(results[0])
        for row_from_db in results:
            # print(row_from_db)
            #creating a dictionary to pass to user contructor
            user_data = {
                'id': row_from_db['users.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'email': row_from_db ['email'],
                'password': row_from_db ['password'],
                'created_at': row_from_db['created_at'],
                'updated_at': row_from_db['updated_at']
            }
            this_show.creator = user.User(user_data)
        return this_show
    

        #the only time 
    # #method to update our 
    # @classmethod
    # def update_pie(cls,data):
    #     query = """ UPDATE PIES
    #                 SET name = %(name)s,
    #                 ingredients = %(ingredients)s,
    #                 size = %(size)s
    #                 Where id = %(id)s;"""
    #     results = connectToMySQL(cls.DB).query_db(query,data)
    #     return results
    

    #validations for creating a new show 
    @staticmethod
    def validate_show(request):
        is_valid =True
        if not request['title']:
            is_valid = False
            flash('Enter a show title', 'create_show_flash')
        
        elif len(request['title']) < 3:
            is_valid = False
            flash('Enter a show with at least 3 characters', 'create_show_flash')

        if not request['network']:
            is_valid = False
            flash('Enter a network', 'create_show_flash')
        
        elif len(request['network']) < 3:
            is_valid = False
            flash('Enter a network with at least 3 characters', 'create_show_flash')
        
        if not request['release_date']:
            is_valid = False
            flash('Enter a  release date', 'create_show_flash')
        
        
        if not (request['comments']):
            is_valid = False
            flash('Enter a comment', 'create_show_flash')

        elif len(request['comments']) < 3:
            is_valid = False
            flash('Enter a comments with at least 3 characters', 'create_show_flash')
            
        return is_valid

    @staticmethod
    def validate_show_edit(request):
        is_valid =True
        if not request['title'].strip():
            is_valid = False
            flash('Enter a show title', 'edit_show_flash')

        
        elif len(request['title']) < 3:
            is_valid = False
            flash('Enter a show with at least 3 characters', 'edit_show_flash')

        if not request['network'].strip():
            is_valid = False
            flash('Enter a network', 'edit_show_flash')
        
        elif len(request['network']) < 3:
            is_valid = False
            flash('Enter a network with at least 3 characters', 'edit_show_flash')
        
        if not request['release_date'].strip():
            is_valid = False
            flash('Enter a  release date', 'edit_show_flash')
        
        
        if not request['comments'].strip():
            is_valid = False
            flash('Enter a comment', 'edit_show_flash')

        elif len(request['comments']) < 3:
            is_valid = False
            flash('Enter a comments with at least 3 characters', 'edit_show_flash')
            
        return is_valid


