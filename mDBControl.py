from pymongo import MongoClient
import json

client = MongoClient()

db = client.foundation

def viewAccount(accountNumber):
    # May have to add an error check for incorect input, or do it above, not sure
    return db.accounts.find_one({'accountNumber': accountNumber})

def loadAccount(filename):
    with open(filename) as file:
        account = json.load(file)
        account["accountNumber"] = getNextAccountNumber()
        db.accounts.insert_one(account)
        return account

def createAccount(account):
    account["accountNumber"] = getNextAccountNumber()
    db.accounts.insert_one(account)
    return account

def deposit(accountNumber, amount):
    total = db.accounts.find_one({'accountNumber': accountNumber})['balance'] + amount
    db.accounts.update_one({'accountNumber': accountNumber}, {"$set": {"balance": total}})
    return db.accounts.find_one({'accountNumber': accountNumber})

def withdarw(accountNumber, amount):
    total = db.accounts.find_one({'accountNumber': accountNumber})['balance'] - amount
    if (total < 0):
        return None
    
    else:
        db.accounts.update_one({'accountNumber': accountNumber}, {"$set": {"balance": total}})
        return db.accounts.find_one({'accountNumber': accountNumber})

def transfer(srcAccount, targAccount, amount):
    sourceTotal = db.accounts.find_one({'accountNumber': srcAccount})['balance'] - amount
    targetTotal = db.accounts.find_one({'accountNumber': targAccount})['balance'] + amount

    if(sourceTotal < 0):
        return None

    else:
        db.accounts.update_one({'accountNumber': srcAccount}, {"$set": {"balance": sourceTotal}})
        db.accounts.update_one({'accountNumber': targAccount}, {"$set": {"balance": targetTotal}})
        return True
    

def delete(accountNumber):
    return db.accounts.delete_one({"accountNumber": accountNumber})

def disconnect():
    client.close()
    print("Closed DB Connection.")

# This querys mongoDB and gets the next account number
def getNextAccountNumber():
    return db.accounts.find().sort("accountNumber", -1).limit(1)[0]["accountNumber"] + 1

