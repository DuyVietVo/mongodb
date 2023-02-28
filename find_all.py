import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['test_container']

for i in mycol.find():
    print(i)