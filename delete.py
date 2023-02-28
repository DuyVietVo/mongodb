import pymongo
#truy van ra id mong muon
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

myquery = {"age": 22}
x = mycol.delete_one(myquery)
print(x.deleted_count,"da xoa")
