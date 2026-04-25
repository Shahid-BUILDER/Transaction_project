from getpass import getpass
from datetime import datetime
import bcrypt
import logging
import os
import time

def login(con):
    cur=con.cursor()
    for _ in range(3):
        user = input("Enter username: ")
        pwd = getpass("Enter password: ").encode('utf-8')
        print("password enetered successfully")
        sql="SELECT password_hash FROM users WHERE user_id=%s"
        cur.execute(sql,(user,))
        result=cur.fetchone()

        if result:
            stored_hash=result[0].encode('utf-8')
            if bcrypt.checkpw(pwd, stored_hash):
                print(" Login successful!")
                logging.info(f"User ID : {user} login successfully!")
                return True
            else:
                print("Wrong password")
        else:
            print(" Invalid credentials.")
            logging.warning(f"An authorized User of ID : {user} attempt to login in the system")
    print(" Too many failed attempts. Exiting...")
    logging.warning(f"Unauthorized user of User ID : {user} attempt to login in the system")
    return False

def record_checking(cur):
    while True:
        try:
            txn_id = int(input("Enter the seat number : "))
            if txn_id <= 0:
                print("Pls enter a positive number")
                continue
            break
        except ValueError:
            print("Pls enter numerical value...")
            logging.error(f"User used invalid user ID : {txn_id}")
    cur.execute("select 1 from users where seat=%s",(txn_id,))
    return (True, txn_id) if cur.fetchone() else (False, txn_id)

def get_valid_date(prompt="Enter Date (DD-MM-YYYY): "):
    while True:
        date_input=input(prompt).strip().replace("\r","").replace("–","-")
        try:
            date_obj=datetime.strptime(date_input, "%d-%m-%Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter as DD-MM-YYYY.")

def clear_load():
    os.system('cls' if os.name == 'nt' else 'clear')
    loading()
    os.system('cls' if os.name == 'nt' else 'clear')

def loading(msg="Loading"):
    print(msg, end="")
    for _ in range(3):
        print(".", end="",flush=True)
        time.sleep(0.5)
    print("fetching data...")
