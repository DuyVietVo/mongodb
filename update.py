import pymongo
#truy van ra id mong muon
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

myquery = {"address": "Nong Son"}
newvalue = {"$set": {"address": "Trung Phuoc, Nong Son"}}

mycol.update_one(myquery, newvalue)

for i in mycol.find():
    print(i)