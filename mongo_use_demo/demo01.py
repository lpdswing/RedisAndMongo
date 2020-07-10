import pymongo
from pymongo import MongoClient

client = MongoClient()

database = client.chapter_3   #client.数据库名
collection = database.example_data_2 # database.集合名
print(database,collection)

# collection.insert_many([
#     {'name':'wm','age':19},
#     {'name':'wm1','age':20},
#     {'name':'wm2','age':21},
#     {'name':'wm3','age':22},
#     {'name':'wm4','age':23},
# ])

rows = collection.find({'age':{'$gt':20}})
for row in rows:
    print(row)

# 按id查
from bson import ObjectId

rows = collection.find({'_id':ObjectId('5f081c6ef60f52aa5f451899')})
print(list(rows))