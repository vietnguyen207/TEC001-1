username = "python"
password = "rules"
attempts = 0
while attempts < 5:
    usern = input("Enter username: ")
    passw = input("Enter password: ")
    if usern == username and passw == password:
        print("Welcome")
        break
    elif usern == username and passw != password:
        print("Your Password is wrong \nPlease Try Again")
        attempts += 1
    elif usern != username and passw == password:
        print("Your username is wrong \nPlease Try Again")
        attempts += 1
    else:
        print("Invalid input! \n Please Try Again")
        attempts += 1
    print("Access Denied!")