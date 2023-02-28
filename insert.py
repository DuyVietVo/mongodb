import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["test_container"]

mylist = [
    {"name": "Loi", "address": "Phu Ninh, Quang Nam","age": 23},
    {"name": "danh", "address": "Phu Ninh, Quang Nam","age": 25},
    {"name": "Thanh", "address": "Phu Ninh, Quang Nam","age": 21},
]

x = mycol.insert_many(mylist)
v = x.inserted_ids
print(v)