username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "Admin":
    if password == "Admin@123":
        print("Hello",username +",","you have successfully logged in")
    else:
        print("Error: Password is not correct.")
else:
    print("Error: Username is not correct.")