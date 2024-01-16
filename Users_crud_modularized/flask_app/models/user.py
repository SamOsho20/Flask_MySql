from flask_app.config.mysqlconnection import connectToMySQL


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
    
    @classmethod
    def get_one(cls,user_id):
        query = """SELECT * FROM users
                WHERE  id = (%(id)s);
        """
        data = {'id' : user_id}
        #instead of stating this in the server.py file we state it here since we logged data as a variable below
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])
    # hey
    @classmethod
    def updating_user(cls,data):
        query = """UPDATE users
            SET first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s
                WHERE  id = %(user_id)s;"""
            #  the last statement before a where clause should never have a comma, s
            # so the email input gets no comma at the end !!
        #instead of stating this in the server.py file we state it here since we logged data as a variable below
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
        


    @classmethod
    def delete_user(cls,id):
        query = """Delete from users
                WHERE  id = %(id)s;"""
        #instead of stating this in the server.py file we state it here since we logged data as a variable below
        results = connectToMySQL(cls.DB).query_db(query,{'id':id})
        return results
        