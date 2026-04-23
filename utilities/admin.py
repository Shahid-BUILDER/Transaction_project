import bcrypt
from colorama import Fore
from getpass import getpass
from utilities.add import add_transaction, add_users
from utilities.display import display_month_transactions, display_user
from utilities.helpers import loading, clear_load, get_valid_date
from utilities.search import search_transaction, search_user
from utilities.update import update_transaction

def menu():
    clear_load()
    while True:
        print("----------------------------------------------------------------------------")
        print("TRANSACTION LOGGER".center(76))
        print("----------------------------------------------------------------------------")
        print("1. Add Records")
        print("2. Display Records")
        print("3. Search Transaction")
        print("4. Update Records")
        print("5. Exit")
        print("----------------------------------------------------------------------------")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-6.")
            continue
        if choice == 1:
            loading()
            while True:
                clear_load()
                print("----------------------------------------------------------------------------")
                print("ADD RECORD SECTION".center(76))
                print("----------------------------------------------------------------------------")
                print("1. Add Transaction")
                print("2. Add Users")
                print("3. Back")
                print("----------------------------------------------------------------------------")
                try:
                    o=int(input("Enter your choice (1-3): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1-6.")
                    continue
                if o==1:    
                    loading()
                    clear_load()
                    month = input("Month name: ").lower()
                    txn_id = input("Transaction ID: ")
                    date_str = get_valid_date("Enter Date (DD-MM-YYYY): ")
                    time_str = input("Time (HH:MM AM/PM): ")
                    try:
                        amount = float(input("Amount: "))
                        add_transaction(month, txn_id, date_str, time_str, amount)
                    except ValueError:
                        print("Invalid format, please enter numeric values only.")
                elif o==2:
                    clear_load()
                    new_user=input("Enter User ID :")
                    user_pass=getpass("Enter user pass: ").encode('utf-8')
                    passw=bcrypt.hashpw(user_pass, bcrypt.gensalt())
                    add_users(new_user,passw)
                elif o==3:
                    break
                else:
                    print("Invalid choice. Try again in range of 1-3.")
                    clear_load()
                    continue
        elif choice == 2:
            loading()
            while True:
                clear_load()
                print("----------------------------------------------------------------------------")
                print("DISPLAY RECORD SECTION".center(76))
                print("----------------------------------------------------------------------------")
                print("1. Display Monthly Transaction")
                print("2. Display User Records")
                print("3. Back")
                print("----------------------------------------------------------------------------")
                try:
                    o=int(input("Enter your choice (1-6): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1-6.")
                    continue
                if o==1:
                    clear_load()
                    month = input("Month name(Month_YR)(eg. January_2026): ").lower()
                    while(True):
                        loading()
                        clear_load()
                        display_month_transactions(month)
                        a=input("For exiting the Display area, please press N/n :")
                        if a=="N" or a=="n":
                            break
                elif o==2:
                    clear_load()
                    while True:
                        loading()
                        clear_load()
                        display_user()
                        a=input("For exiting the Display area, please press N/n: ")
                        if a=="N" or a=="n":
                            break
                elif o==3:
                    break
                else:
                    print("Invalid choice. Try again in range of 1-2.")
                    clear_load()
                    continue
        elif choice == 3:
            loading()
            while True:
                clear_load()
                print("----------------------------------------------------------------------------")
                print("SEARCH RECORD SECTION".center(76))
                print("----------------------------------------------------------------------------")
                print("1. Search Transaction")
                print("2. Search Users")
                print("3. Back")
                print("----------------------------------------------------------------------------")
                try:
                    o=int(input("Enter your choice (1-6): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1-6.")
                    continue
                if o==1:
                    clear_load()
                    month = input("Month name(Month_YR)(eg. January_2026): ").lower()
                    txn_id = input("Transaction ID: ")
                    loading()
                    clear_load()
                    search_transaction(month, txn_id)
                    a=input("For exiting the Display area, please press N/n: ")
                    if a=="N" or a=="n":
                        break
                elif o==2:
                    clear_load()
                    user_id=input("Enter the user id : ")
                    loading()
                    table="users"
                    search_user(table, user_id)
                    if a=="N" or a=="n":
                        break
                elif o==3:
                    break
                else:
                    print("Invalid choice. Try again in range of 1-2.")
                    clear_load()
                    continue
        elif choice == 4:
            loading()
            clear_load()
            print("----------------------------------------------------------------------------")
            print("UPDATE RECORD SECTION".center(76))
            print("----------------------------------------------------------------------------")
            print("1. Update Transaction")
            print("2. Update Users")
            print("3. Back")
            print("----------------------------------------------------------------------------")
            try:
                o=int(input("Enter your choice (1-6): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1-6.")
                continue
            if o==1:
                clear_load()
                month = input("Month name: ").lower()
                txn_id = input("Transaction ID: ")
                new_date = get_valid_date("Enter new Date (DD-MM-YYYY): ")
                new_time = input("Enter new Time (HH:MM AM/PM): ")
                new_amount = input("New Amount: ")
                try:
                    new_amount = float(new_amount) if new_amount else None
                except ValueError:
                    print("Invalid format, please enter numeric values only.")
                    new_amount = None
                update_transaction(month, txn_id, new_date, new_time or None, new_amount)
            elif o==2:
                print()
            elif o==3:
                break
            else:
                print("Invalid choice. Try again in range of 1-2.")
                clear_load()
                continue
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
            clear_load()
            continue