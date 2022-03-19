def menu():
    print("1. Load")
    print("2. Show")
    print("0. Exit")
    
    try: 
        option = int(input("Select menu option: "))

    except:
        option = -1

    return option

def main():
    while(True):
        optionSelected = menu()
        if(optionSelected == 0):
            print("Exiting...")
            break

        if(optionSelected == 1):
            print("You selected option 1 to load data...")
        elif(optionSelected == 2):
            print("You selected option 2 to show data...")
        else:
            print("Invalid option. Try again...")

if __name__ == "__main__":
    main()