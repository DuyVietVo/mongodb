import pymongo
#truy van ra id mong muon
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

x = mycol.find().sort("name",-1)

for i in x:
    print(i)