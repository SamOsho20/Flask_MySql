from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import comment
import re

    
class Comment:
    DB = 'netflix_schema'
    def __init__(self,data):
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.show_id = data['show_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        
    @classmethod
    def show_this_shows_comment(cls,data):
        query = """SELECT * FROM COMMENTS
                    join shows on comments.show_id = shows.id
                    join users on comments.user_id = users.id
                    where shows.id = %(id)s;
                """
        results =  connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def create_comment(cls,data):
        query = """INSERT INTO comments (comment,show_id,user_id) 
        values (%(comment)s, %(show_id)s, %(user_id)s);"""
        results =  connectToMySQL(cls.DB).query_db(query,data)
        return results


    
    
    
    