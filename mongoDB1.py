import pymongo

client = pymongo.MongoClient("mongodb+srv://iNeuron:ammaacha@ineuron.xhlnnwu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {'name': 'Pradeep',
      'email': 'sffrg@sagf.com',
      'phno': 34251345
    }

db1 = client['mongoDB']
coll = db1['test']
coll.insert_one(d)