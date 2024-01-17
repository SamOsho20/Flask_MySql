# We need to import the burger class from our models
from flask_app.models import ninja
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    DB = "dojos_ninjas_schema2"
    def __init__(self, data ):
            self.id = data['id']
            self.name = data['name']
        
        # We create a list so that later we can add in all the ninjas that are associated with a dojos.
            self.ninjas = []
    @classmethod
    def save (cls, data ):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL(cls.DB).query_db( query, data)
        return results
    
    @classmethod
    def get_all_dojos (cls):
        query = "SELECT * FROM dojos;"
        results =  connectToMySQL(cls.DB).query_db( query)
        all_dojos = []
        for dojos in results:
            all_dojos.append(cls(dojos))
        return all_dojos
    


    @classmethod
    def get_dojos_with_ninjas(cls, data ):
        # query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojo.id WHERE dojo.id = %(id)s;"
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"

        #left join will grab everything regrdless of a relationship  a relationship 
            # -(so it will get all ninjas regradless if theres a dojo or not  )
        #Regular join will grab everthing where there is only a relationshio 
            # so it would only grab the ninjas assscoiated to the boston, indiana dojo or etc
        results = connectToMySQL(cls.DB).query_db(query, data )
        # results will be a list of topping objects with the ninjas attached to each row. 
        dojo = cls(results[0])
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "name": row_from_db["ninjas.name"],
                "full_name": row_from_db["full_name"],
                "email": row_from_db["email"],
                "age": row_from_db["age"],
                "created_at": row_from_db[".created_at"],
                "updated_at": row_from_db["dojos.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
            #here we are saying our ninjas instance above is going to be combined with our Ninja instances from the ninja
            # file and then well return that entire list of its contents
        return Dojo
    