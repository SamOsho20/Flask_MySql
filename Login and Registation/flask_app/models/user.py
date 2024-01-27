from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = 'loginandreg_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO USER
                    (first_name,last_name,email,password,created_at,updated_at) 
                    VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());
                    """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def get_one_user(cls,user_id):
        query = """SELECT * FROM USER
                    Where id = %(user_id)s;
                    """
                    #make sure names match up for id like above on lines 29,31, "user_id"
        results = connectToMySQL(cls.DB).query_db(query,user_id)
        return cls(results[0])
    

    #  'bool' object is not subscriptable error 
    # return cls(results[0])
    # another name for iterating is subscripting !!


    @staticmethod
    def validate_registration(request):
        is_valid = True
        if not request['email']:
            is_valid = False
            flash('Enter a Email', 'reg_flash')

        elif not EMAIL_REGEX.match(request["email"]):
            is_valid = False
            flash('invalid email address', 'reg_flash')

        if not request['first_name']:
            is_valid = False
            flash('Enter a First Name', 'reg_flash')

        elif len(request["first_name"])< 2:
            is_valid = False
            flash('First Name must be at least 2 characters', 'reg_flash')

        if not request['last_name']:
            is_valid = False
            flash('Enter a Last Name', 'reg_flash')

        elif len(request["last_name"])< 2:
            is_valid = False
            flash('Last Name must be at least 2 characters', 'reg_flash')

        if not request['password']:
            is_valid = False
            flash('Enter A password', 'reg_flash')

        elif len(request["password"])< 8:
            is_valid = False
            flash('Password Must Be over 8 characters', 'reg_flash')
        
        if request['password'] != request['confirm_password']:
            is_valid = False
            flash('Passwords Dont Match', 'reg_flash')

        return is_valid
        #must have return is_valid!!!!!!!
    