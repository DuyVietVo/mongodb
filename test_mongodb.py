import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['test_container']


x= mycol.find_one()

print(x)
