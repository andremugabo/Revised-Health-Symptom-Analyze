import os
import csv
import constant


def initialize_files():
    #Create users file if not exist
    if not os.path.exists(constant.USERS_FILE):
        with open(constant.USERS_FILE, 'w',newline='') as file:
            write = csv.writer(file)
            write.writerow(["username","name","dob","password"])