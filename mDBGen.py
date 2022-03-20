from pymongo import MongoClient
from random import randint

client = MongoClient()

db = client.foundation

names = ['Mark', 'Amber', 'Todd', 'Anita', 'Sandy', 'Divna', 'Katla', 'Maynard', 'Xavier', 'Kyo', 'Alice', 'Sophie', 'Dale', 'Gus', 'Alec', 'Matt', 'Eddie']

for ac in range(1,8):   # Note this only really works if there are no accounts in the DB yet
    account = {
        'accountNumber' : ac,
        'name' : names[randint(0, (len(names)-1))],
        'balance' : randint(0, 10000) + (randint(0, 99) * 0.01)
    }

    result = db.accounts.insert_one(account)

    print(f"Created {ac} of 7 as {result.inserted_id}.")

print("Finished creating 7 bank accounts")
