menu = ""

while menu != "1" or menu != "2":
    print("Would you like to save a new password or view your old ones :-")
    print("1)\t Input new password.")
    print("2)\t View passwords.")
    print("3)\t Quit!")
    menu = input()
    if menu == "1":
        software_name = input("Enter the name of the software :- ")
        username = input("Enter the username :- ")
        password = input("Enter the password :- ")
        file = open("secure_password_data.txt", "a")
        file.write("Software Name : " + software_name + "\nUsername :" + username + "\nPassword : " + password)
        file.write("\n---------------------------------------------------------------------------\n")
        file.close()
    elif menu == "2":
        print("Passwords :-")
        file = open("secure_password_data.txt", "r")
        for i in file:
            print(i)
    elif menu == "3":
        exit()
