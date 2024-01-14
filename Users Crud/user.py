from mysqlconnection import connectToMySQL


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

    @classmethod
    def update(cls,data):
        query = """UPDATE users
            SET first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s,

                WHERE  id = %(id)s;
        """
        #instead of stating this in the server.py file we state it here since we logged data as a variable below
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
        