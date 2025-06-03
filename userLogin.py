import getpass
import constant
import csv


def login_user():
    print("\n--- Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")


    with open(constant.USERS_FILE,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[3] == password:
                print(f"Welcome back, {row[1]} !")
                return {"username":row[0], "name":row[1], "dob":row[2]}
    print("Invalid username or password!")
    return None        