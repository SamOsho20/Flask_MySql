from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    DB = "dojos_ninjas_schema2"
    def __init__(self, data ):
            self.id = data['id']
            self.name = data['name']
            self.name = data['location']
        
        # We create a list so that later we can add in all the burgers that are associated with a restaurant.
            self.burgers = []
    @classmethod
    def save (cls, data ):
        query = "INSERT INTO restaurants (name,location) VALUES (%(name)s,%(location)s);"
        return connectToMySQL(cls.DB).query_db( query, data)

