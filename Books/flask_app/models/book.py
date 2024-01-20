from flask_app.config.mysqlconnection import connectToMySQL
class Books:
    def __init__(self,data):
        self.id = data['id'],
