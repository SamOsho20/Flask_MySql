from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB = "dojos_ninjas_schema2"
    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        #i dont understand why we wouldn't  enter an instance for the dojo_id here,
        #  its a column in our sql so why wouldn't it be logged here???

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (full_name, email, age,dojo_id, created_at, updated_at ) VALUES (%(full_name)s, %(email)s, %(age)s,%(dojo_id)s, NOW(), NOW());"
        #we accept the dojo_id (foreign key ) here in the query statement and
        #  dont need to pass it into the class as an instance
        return connectToMySQL(cls.DB).query_db(query, data)
    
    