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
    total = amount + db.accounts.find_one({'accountNumber': accountNumber})['balance']
    db.accounts.update_one({'accountNumber': accountNumber}, {"$set": {"balance": total}})
    return db.accounts.find_one({'accountNumber': accountNumber})

def withdarw(accountNumber, amount):
    pass

def transfer(srcAccount, targAccount, amount):
    pass

def delete(accountNumber):
    pass

# This querys mongoDB and gets the next account number
def getNextAccountNumber():
    return db.accounts.find().sort("accountNumber", -1).limit(1)[0]["accountNumber"] + 1

