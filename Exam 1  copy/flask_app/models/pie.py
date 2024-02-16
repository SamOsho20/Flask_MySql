from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
import re


class Pie:
    DB = 'userandpie_schema'
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.ingredients = data['ingredients']
        self.size = data['size']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None


    @classmethod
    def create_new_pie(cls,data):
        query ="""INSERT INTO pies 
            (user_id,name,ingredients,size,created_at, updated_at)
            values (%(user_id)s,%(name)s, %(ingredients)s,%(size)s,NOW(),NOW());"""
        results = connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_pie(cls,id):
        query = """DELETE FROM PIES WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,{'id':id})
        return results
    
    @classmethod
    def update_pie(cls,data):
        query = """ UPDATE PIES
                    SET name = %(name)s,
                    ingredients = %(ingredients)s,
                    size = %(size)s
                    Where id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    

        
    @classmethod
    def get_one_pie(cls,id):
        query = """SELECT *    
                    FROM pies 
                    JOIN users
                    ON pies.user_id = users.id
                    Where pies.id = %(id)s;
                    """
                    #make sure names match up for id like above on lines 29,31, "user_id"
        results = connectToMySQL(cls.DB).query_db(query,id)
        this_pie = cls(results[0])
        for row_from_db in results:
            # print(row_from_db)
            #creating a dictionary to pass to user contructor
            user_data = {
                'id': row_from_db['users.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'email': row_from_db ['email'],
                'password': row_from_db ['password'],
                'created_at': row_from_db['users.created_at'],
                'updated_at': row_from_db['users.updated_at']
            }
            this_pie.creator = user.User(user_data)
        return this_pie
        #the only time you need to return results is on a insert query where you are returning the id 
    @classmethod
    def get_all_pies_and_users(cls):
        query = """SELECT *
                    FROM pies 
                    JOIN users
                    ON pies.user_id = users.id;
                """
                #make sure all your query statements are  all lower case for line 64 - 68
                #query to get all pies with users that made it!!

        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        output = []
        for row_from_db in results:
            this_pie = cls(row_from_db)
            # print(row_from_db)
            #creating a dictionary to pass to user contructor
            user_data = {
                'id': row_from_db['users.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'email': row_from_db ['email'],
                'password': row_from_db ['password'],
                'created_at': row_from_db['users.created_at'],
                'updated_at': row_from_db['users.updated_at']
            }
            this_pie.creator = user.User(user_data)
            #makes a user object 
            output.append(this_pie)
        # print(output)
        return output

    
    
    
    @staticmethod
    def validate_new_pie(request):
        is_valid = True
        if not request['name']:
            is_valid = False
            flash('Enter a pie name', 'new_pie_flash')
        if not request['ingredients']:
            is_valid = False
            flash('Enter pie ingredients', 'new_pie_flash')
        if not request['size']:
            is_valid = False
            flash('enter pie size', 'new_pie_flash')
        
    @staticmethod
    def validate_updated_pie(request):
        is_valid = True
        if not request['name']:
            is_valid = False
            flash('Enter a pie name', 'update_pie_flash')
        if not request['ingredients']:
            is_valid = False
            flash('Enter pie ingredients', 'update_pie_flash')
        if not request['size']:
            is_valid = False
            flash('enter pie size', 'update_pie_flash')

        return is_valid
    
    
    #  results = connectToMySQL (cls.DB).query_db(query,user_id)
    #     our_pie = cls (results[0])
    #     print(our_pie)
    #     for row_from_db in results:
    #         print(row_from_db)
            
    #         pie_data ={
    #             'id': row_from_db['pies.id'],
    #             'user_id': row_from_db['user_id'],
    #             'name': row_from_db['name'],
    #             'ingredients': row_from_db ['ingredients'],
    #             'size': row_from_db ['size'],
    #             'created_at': row_from_db['pies.created_at'],
    #             'updated_at': row_from_db['pies.updated_at']

    #             }
    #         our_pie.this_pie.append(pie.Pie(pie_data))
    #     return our_pie
    # # @classmethod
    # def get_pie_with_user_id(cls,user_id):
    #     query = """select * from users
    #                 join pies on users.id = pies.user_id
    #                 where users.id = %(user_id)s
    #                 """
    #     results = connectToMySQL (cls.DB).query_db(query,user_id)
    #     this_user = cls (results[0])
    #     print(this_user)
    #     for row_from_db in results:
    #         print(row_from_db)
            
    #         user_data ={
    #             'id': row_from_db['user.id'],
    #             'first_name': row_from_db['first_name'],
    #             'last_name': row_from_db ['last_name'],
    #             'email': row_from_db ['email'],
    #             'password': row_from_db['password'],
    #             'created_at': row_from_db['user.created_at'],
    #             'updated_at': row_from_db['users.updated_at']

    #             }
    #         this_user.creator.append(user.User(user_data))
    #     return this_user

    

