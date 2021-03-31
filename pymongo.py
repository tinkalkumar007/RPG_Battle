import pymongo
from pymongo import MongoClient
myclient=pymongo.MongoClient("mongodb://localhost:27017")
# MongoClient is an object 
mydb=myclient["mydatabase"]
# generate a table to store data in localhost adress.
mycol=mydb["customers"]
#mongoDB waits until you have created a collection(table), with atleast one document before it actally create db.
mydict={"name":"john","adress":"Noida sector 27"}
# data collection
x=mycol.insert_one(mydict)
#insert_one used to insert a record into a collection.insert_many to insert no of record
