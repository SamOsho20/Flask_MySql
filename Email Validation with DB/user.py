from mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

#we must import re for validation of email!
#we must import flash to use it 

class User:
    DB = "users_cr_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # read
    @classmethod
    def get_all_users(cls):
        query=" SELECT * FROM Users;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_users = []
        for user in results:
            all_users.append(cls(user))
        return all_users
    
    # create
    @classmethod
    def save(cls, data):
        query="""INSERT INTO Users (first_name, last_name, email, created_at) 
                VALUES (%(first_name)s,%(last_name)s,%(email)s,now());"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    

    # adding form validation 
    #need to be a static method because it doesnt apply directly to the class
    #we use class methods when we need acess to the constructor (cls) that houses a method,
    # since we dont need that for this we use a static method 

    @staticmethod
    #static methods dont get inferred first arguments 
    def validate_user(request):
        print("im here ")
        is_valid = True
        #establishing a boolean 
        #validation for first name 
        if not request['first_name'] :
            is_valid = False
            flash("please provide a first name", "f_name")
            #so if the user inputs nothing we flash message above 
            # the f_name variable is the same variable we run on give to category_filter one line 21 to print this message 
        elif len(request['first_name']) < 3:
            is_valid = False
            flash("please provide a longer  first name", "f_name")
            # we can alo use elif to have a more in depth flash message to user 
            print(is_valid)

        #validation for last  name 
        if not request['last_name']:
            is_valid = False
            flash("please provide a last name", "f_name")
            #so if the user inputs nothing we flash message above 
            # the f_name variable is the same variable we run on give to category_filter one line 21 to print this message 
        elif len(request['last_name']) < 2:
            is_valid = False
            flash("please provide a longer last name", "f_name")
            # we can alo use elif to have a more in depth flash message to user 
            #??? for some reason when i enter lengths for first name and last name less tan 2 only 
            # get a response saying the last name needs to be longer
            print(is_valid)

        if not request['email']:
            is_valid = False
            flash ('please enter an email', 'f_name')
            #if theres no email input well have nothing to validate so this message is needed 
        elif not EMAIL_REGEX.match(request['email']):
            #so if our email input doesnt match the regex format above this will be false and get teh flash message
            flash("invalid email address, please try again", 'f_name')
            is_valid = False
        return is_valid
