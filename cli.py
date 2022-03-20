from mDBControl import viewAc

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
        if(optionSelected == 0):
            print("Exiting...")
            break

        if(optionSelected == 1):
            print("You selected \"Create Account\".")
            pass        # call create function here

        elif(optionSelected == 2):
            print("You selected \"View Account\".")
            try:
                num = int(input("Enter account number: "))
                account = viewAc(num)       # viewAc is trying to find the record in the DB with the given account number
            
            except:
                account = None

            if(account):
                print(f"Account Number: {account['accountNumber']}")
                print(f"Name: {account['name']}")
                print(f"Balance: ${account['balance']}")

            else:
                print(f"Could not find account number: {num}")

        elif(optionSelected == 3):
            print("You selected \"Deposit\".")
            pass        # call Deposit function here

        elif(optionSelected == 4):
            print("You selected \"Withdraw\".")
            pass        # call Withdraw function here

        elif(optionSelected == 5):
            print("You selected \"Transfer\".")
            pass        # call Transfer function here

        elif(optionSelected == 6):
            print("You selected \"Delete Account\".")
            pass        # call Delete function here

        elif(optionSelected == 7):
            print("You selected \"Load Account\".")
            pass        # call Load function here

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()