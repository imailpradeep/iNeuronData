import pymongo

client = pymongo.MongoClient("mongodb+srv://iNeuron:ammaacha@ineuron.xhlnnwu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
