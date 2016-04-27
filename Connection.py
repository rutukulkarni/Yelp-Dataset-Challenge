from pymongo import MongoClient

class Connection:

    def connect(self):
        connection = MongoClient()
        connection = MongoClient('localhost', 27017)
        db = connection.DataDiningDB
        return db
