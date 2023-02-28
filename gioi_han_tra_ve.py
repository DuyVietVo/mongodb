import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

myresult = mycol.find().limit(2)
# lay ra 2 ket qua 
for i in myresult:
    print(i)