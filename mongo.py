import pymongo
# from pymongo import MongoClient 

cluster = pymongo.MongoClient("mongodb+srv://mcpython:mcpython123@cluster0.vqetj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #establising mongodb connection
db = cluster["minecraft"] #database name from MongoDB
collection = db["server-logs"]

# post = {"_id": 1, "name":"test1"}
# collection.insert_one(post)






