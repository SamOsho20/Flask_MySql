from mysqlconnection import connectToMySQL


class Friend:
    DB = "first_flask"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # the save method will be used when we need to save a new friend to our database
    #create
    @classmethod
    def save(cls, data):
        query = """INSERT INTO friends (first_name, last_name, occupation)
    	VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    #read
    @classmethod
    #since we are only looking to get the id we will ad it as an argument 
    def get_one_friend(cls, id):
        query= """" SELECT * FROM friends 
                    WHERE id = (%(id)s)
                """
        results = connectToMySQL(cls.DB).query_db(query, {"id":id})
        # we are expecting back  list of dictionary from the id 
        # although we will only get back one number still a part of a dictionary 
        return cls(results[0])
        # this does not make sense to me. is the number 0 gonna be teh id number entered?
        # so basically the only argument that results takes is from  {"id":id}???

    #read but for a get_all
    @classmethod
    #we dont need to enter data to select all from something
    def get_all_friends(cls):
        query=" SELECT * FROM friends "
        results = connectToMySQL(cls.DB).query_db(query)
        # # so we will collect a list of dictionarys 
        # with all the friend data represented as dictionarys 
        # we want to sort our dictionary so it can be easily sorted in the server so we 
        list_friends = []
        for row in results:
        # for each row in the dictionary we will make a object 
            list_friends.append(cls(row))
            # and put those objects in a list 
        return list_friends
        


