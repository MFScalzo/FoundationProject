from pymongo import MongoClient
from random import randint
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


def generate(n):
    print("Deleting all bank accounts in Database...")
    result = db.accounts.delete_many({})
    print(f"{result.deleted_count} documents deleted.")

    names = ['Mark', 'Amber', 'Todd', 'Anita', 'Sandy', 'Divna', 'Katla', 'Maynard', 'Xavier', 'Kyo', 'Alice', 'Sophie', 'Dale', 'Gus', 'Alec', 'Matt', 'Eddie', 'Clark', 'Olivia', 'Eli']

    print(f"Generating {n} new bank accounts...")

    for ac in range(1,n+1):
        account = {
            'accountNumber' : ac,
            'name' : names[randint(0, (len(names)-1))],
            'balance' : randint(0, 10000) + (randint(0, 99) * 0.01)
        }

        result = db.accounts.insert_one(account)

        print(f"Created {ac} of {n} as {result.inserted_id}.")

    print(f"Finished creating {n} bank accounts")


def analyze():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("What analysis do you want to generate?")
    print("1. Largest Balance")
    print("2. Smallest Balance")
    print("3. Average Balance")
    print("0. Cancel")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try:
        option = int(input("Select menu option: "))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    except:
        option = 0

    if(option == 1): # Account with Largest Balance
        result = db.accounts.find().sort("balance", -1).limit(1)[0]

        print(f"Account Number: {result['accountNumber']}")
        print(f"Name: {result['name']}")
        print(f"Balance: ${result['balance']}")

    if(option == 2): # Account with the Smallest Balance
        result = db.accounts.find().sort("balance", 1).limit(1)[0]

        print(f"Account Number: {result['accountNumber']}")
        print(f"Name: {result['name']}")
        print(f"Balance: ${result['balance']}")

    if(option == 3): # Average Account Balance
        pipeline = [{'$group': {'_id': 'null', 'avgBalance': {'$avg': '$balance'}}}]
        result = list(db.accounts.aggregate(pipeline))

        print(f"Average Account Balance: ${round(result[0]['avgBalance'], 2)}")

    