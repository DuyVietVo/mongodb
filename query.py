import pymongo
#truy van ra id mong muon
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

myquery = {"age": 22}

mydoc = mycol.find(myquery)

for i in mydoc:
    print(i)