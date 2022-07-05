contacts = {}

while(True):
    print("\n1. Add contact\n2. See contacts\n3. Search for contact \n4. Exit")
    try:
        selection = int(input())
        if (selection == 1):
            name = input("Enter name: ")
            if (name in contacts):
                print("this name is already taken")
            else:
                while(True):
                    number = int(input("Enter number: "))
                    if (number >= 1000000000 and number <= 9999999999):
                        contacts[name] = number
                        break
                    else:
                        print("Please Enter valid mobile number")
        elif (selection == 2):
            print(contacts)
        elif (selection == 3):
            name = input("Enter name to search: ")
            if (name in contacts):
                print(contacts[name])
            else:
                print("no contact found with the name")
        elif selection == 4:
            exit()

    except ValueError as err:
        print(err)
        print("Please Enter integer values")
