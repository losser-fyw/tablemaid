import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatebase"]
mycol=mydb["notes"]
dict={"_id":0,"hour":8,"minute":30}
for i in mycol.find():
    if dict["_id"]==i["_id"]:
        x=mycol.delete_one(i)
        mycol.insert_one(dict)
    else:
        mycol.insert_one(dict)

for x in mycol.find():
    print(x)

