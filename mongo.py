import json
import pymongo 

client = pymongo.MongoClient('mongodb://hora:hora@ds111798.mlab.com:11798/timestamps')
db = client.get_database()

# json.loads](str( page.fetch()  ))

cursor  = db.items.find( { 'price': { '$gt': 5000, '$lt': 5500 } }).skip(0).limit(25)
for i in cursor:
  print(i['id'], i['title'], i['price'])  
  
dir(cursor)
cursor.count()