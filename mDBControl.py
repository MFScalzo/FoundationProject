from pymongo import MongoClient

client = MongoClient()

db = client.foundation

def viewAc(accNum):
    # May have to add an error check for incorect input, or do it above, not sure
    return db.accounts.find_one({'accountNumber': accNum})


#print(type(viewAc(100)))