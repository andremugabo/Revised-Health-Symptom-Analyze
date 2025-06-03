import os
import csv
import constant
import getpass


def register_user():
    print("\n--- Registration ---")
    username = input("Enter username: ")


    #Check if username already exists
    if os.path.exists(constant.USERS_FILE):
        with open(constant.USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    print("Username already exists!")
                    return
                
    name = input("Enter your full name: ") 
    dob = input("Enter your date of birth (YYYY-MM-DD): ") 
    password = getpass.getpass("Enter password: ")   

    with open(constant.USERS_FILE, 'a', newline='') as file:
        write = csv.writer(file)
        write.writerow([username,name,dob,password]) 

    print("User Registered successfully ")          