from colorama import Fore
from utilities.add import add_transaction
from utilities.display import display_month_transactions
from utilities.helpers import loading, clear_load, get_valid_date
from utilities.search import search_transaction
from utilities.update import update_transaction

def U_menu():
    clear_load()
    while True:
        print("----------------------------------------------------------------------------")
        print("TRANSACTION LOGGER".center(76))
        print("----------------------------------------------------------------------------")
        print("1. Add Transaction")
        print("2. Display Month Transactions")
        print("3. Search Transaction")
        print("4. Update Transaction")
        print("5. Exit")
        print("----------------------------------------------------------------------------")
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-6.")
            continue
        if choice == 1:
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
        elif choice == 2:
            clear_load()
            month = input("Month name(Month_YR)(eg. January_2026): ").lower()
            while(True):
                loading()
                clear_load()
                display_month_transactions(month)
                a=input("For exiting the Display area, please press N/n :")
                if a.lower()=='n':
                    break
        elif choice == 3:
            clear_load()
            month = input("Month name(Month_YR)(eg. January_2026): ").lower()
            txn_id = input("Transaction ID: ")
            loading()
            clear_load()
            search_transaction(month, txn_id)
        elif choice == 4:
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
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
            clear_load()
            continue