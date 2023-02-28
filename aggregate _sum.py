import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["aggregate"]


price_result = mycol.aggregate(
    [{"$facet":{
        "sort_price":[{"$sort": {"price": 1}}],
        "count":[ {"$count":"total"}],
    }
   } ]
    
)
for i in price_result:
    print(i)
    