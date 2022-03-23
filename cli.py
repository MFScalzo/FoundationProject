from mDBControl import viewAccount, loadAccount, createAccount, deposit, withdarw, transfer, delete

def menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please choose an option:")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Delete Account")
    print("7. Load Account")
    print("0. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try: 
        option = int(input("Select menu option: "))

    except:
        option = -1

    return option

def main():
    print("########################################")
    print("    Welcome to the Bank Teller CLI!")
    print("########################################")

    while(True):
        optionSelected = menu()
        
        if(optionSelected == 0):        # EXIT
            print("Exiting...")
            break

        if(optionSelected == 1):        # CREATE ACCOUNT
            print("You selected \"Create Account\".")
            
            try:
                accName = str(input("Enter Name on Account: "))
                accBalance = round(float(input("Enter starting Balance: $")), 2)
                newAccount = {'name': accName, 'balance': accBalance}
                newAccount = createAccount(newAccount)       # Creating account with given data

                print(f"Name on account: {newAccount['name']}")
                print(f"Balance: ${newAccount['balance']}")
                print(f"Account Number: {newAccount['accountNumber']}")
                
            except:
                print("Please Enter Valid Information.")

            wait()

        elif(optionSelected == 2):      # VIEW ACCOUNT
            print("You selected \"View Account\".")

            try:
                accountNumber = int(input("Enter account number: "))
                account = viewAccount(accountNumber)
            
            except:
                account = None

            if(account):
                print(f"Account Number: {account['accountNumber']}")
                print(f"Name: {account['name']}")
                print(f"Balance: ${round(account['balance'], 2)}")

            else:
                print(f"Could not find account number: {accountNumber}")

            wait()

        elif(optionSelected == 3):      # DEPOSIT
            print("You selected \"Deposit\".")
            
            try:
                accountNumber = int(input("Account Number to Deposit to: "))
                amount = round(float(input("Amount to Deposit: $")), 2)

                if(amount < 0):
                    raise Exception("Deposit can't be Negative.")

                account = deposit(accountNumber, amount)

            except Exception as e:
                print("Error while depositing.")
                print(e)

            else:
                print(f"New Balance: ${account['balance']}")

            wait()

        elif(optionSelected == 4):      # WITHDRAW
            print("You selected \"Withdraw\".")
            
            try:
                accountNumber = int(input("Account Number to Withdraw from: "))
                amount = round(float(input("Amount to Withdraw: $")), 2)

                if(amount < 0):
                    raise Exception("Withdrawal cannot be Negative.")

                account = withdarw(accountNumber, amount)

                if(not account):
                    raise Exception("Insufficient funds for withdrawal.")

            except Exception as e:
                print("Error while withdrawing.")
                print(e)

            else:
                print(f"New Balance: ${account['balance']}")

            wait()

        elif(optionSelected == 5):      # TRANSFER
            print("You selected \"Transfer\".")
            
            try:
                sourceAccount = int(input("Account to withdraw from: "))
                targetAccount = int(input("Account to deposit to: "))
                amount = round(float(input("Amount to transfer: $")), 2)

                if(amount < 0):
                    raise Exception("Transfer cannot be Negative.")

                result = transfer(sourceAccount, targetAccount, amount)

                if(not result):
                    raise Exception(f"Insufficient funds in Account: {sourceAccount}")

            except Exception as e:
                print("Error while transfering.")
                print(e)

            else:
                print(f"${amount} transfered from account {sourceAccount} to account {targetAccount}.")

            wait()

        elif(optionSelected == 6):      # DELETE
            print("You selected \"Delete Account\".")
            accountNumber = int(input("Account Number to Delete: "))
            result = delete(accountNumber)
            print(f"Account Number {accountNumber} deleted.")

            wait()

        elif(optionSelected == 7):      # LOAD
            print("You selected \"Load Account\".")
            accFile = input("Bank Account File to Load: ")

            try:
                acc = loadAccount(accFile)

                print("New Account Created!")
                print(f"Account Number: {acc['accountNumber']}")
                print(f"Name: {acc['name']}")
                print(f"Balance: {acc['balance']}")

            except:
                print("New Account could not be Loaded.")
            
            wait()

        else:
            print("Invalid option. Try again.")

def wait():
    input("Enter to continue...")

if __name__ == "__main__":
    main()
