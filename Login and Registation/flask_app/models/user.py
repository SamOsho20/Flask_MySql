from flask_app.config.mysqlconnection import connectToMySQL


class User:
    DB = 'loginandreg_schema'
    def __init__(self,data):
        self.name = data['name']