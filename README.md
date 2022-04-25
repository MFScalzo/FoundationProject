# Bank Teller CLI

## Description
A Python CLI (Command Line Interface) application for a Bank Teller. This application allows the user to Create, View, Delete, and Analyze Bank Accounts stored in a MongoDB database. It also provides the functionality to Deposit, Withdraw, and Transfer funds between the bank accounts. Finally, you can also Load Bank Account info from a JSON file.

## Technologies Used
- Python - version 3.9.10
- MongoDB - version 5.06 Community
- PyMongo - 4.02
- git - version 2.35.1.windows.2

## Features
- Create an account
- View an account
- Deposit to an account
- Withdraw from an account
- Transfer from one account to another
- Delete an account from the database
- Load an account from a .json file
- Analyze all accounts in the database

## Getting Started
You will need to install MongoDB Server 5.0 for your operating system:

https://www.mongodb.com/docs/manual/installation/

To download the repo files, type:

    git clone https://github.com/MFScalzo/FoundationProject.git
    
Install PyMongo:

    pip install pymongo

### Windows
Create the directory where MongoDB will store it's files (this is the default location):

    cd C:\
    md data\db

Run MongoDB Server in its own CMD window (if you created the data directory in the default location):

    cd 'C:\Program Files\MongoDB\Server\5.0\bin\'
    mongod.exe
    
Run MongoDB Server in its own CMD window (if you created the data directory in a different location use --dbpath=""):

    & "C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe" --dbpath="<path to data folder>"

### Ubuntu
Run MongoDB Server:

    sudo systemctl start mongod

## Usage
To run the program, navigate to the repo directory, then execute cli.py in its own window:

    cd C:\path\to\FoundationProject
    python cli.py

While the program is running you can choose what action you want to take by picking one of the numbered options:

![CLI Welcome Screen](https://raw.githubusercontent.com/MFScalzo/FoundationProject/main/images/Welcome.png)

When picking a .json file to import make sure you type the entire file name:

![CLI Load from JSON](https://raw.githubusercontent.com/MFScalzo/FoundationProject/main/images/LoadAccount.png)

## License
This project uses the following license: [MIT License](https://github.com/MFScalzo/FoundationProject/blob/main/LICENSE.txt)
