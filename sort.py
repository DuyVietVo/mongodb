import pymongo
#truy van ra id mong muon
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

mydoc = mycol.find().sort("name")

for row in mydoc:
    print(row)