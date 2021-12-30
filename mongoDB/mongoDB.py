import pymongo
from pymongo import MongoClient

URL = 'mongodb+srv://admin:admin@cluster0.ybboc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = MongoClient(URL)
db = client['local']
collection = db['my_sample']

print('ok')


