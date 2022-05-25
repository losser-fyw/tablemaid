import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatebase"]
mycol=mydb["notes"]
mycol1=mydb["alarm"]
#mycol.delete_many({})
mycol.update_one({"_id":1},{"$set": {"first":1}})
for i in mycol.find():
    print(i)
