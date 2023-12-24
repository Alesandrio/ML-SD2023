from pymongo import MongoClient

class LoadData:
    def __init__(self):
        pass

    def connect(self, url:str):
        self.client = MongoClient(url)
        print('Connected...')
    
    def disconnect(self):
        self.client.close()
        print('Connection closed...')