import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatebase"]
mycol=mydb["notes"]
mycol1=mydb["alarm"]
mycol.drop()