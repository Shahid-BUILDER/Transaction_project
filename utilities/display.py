from db_config import connect_to_db
from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

def display_month_transactions(month_name):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute(f"""
        SELECT date_entry, transaction_id, time_entry, amount
        FROM `{month_name}`
        ORDER BY date_entry, time_entry
    """)
    data = cur.fetchall()
    con.close()

    if not data:
        print(Fore.YELLOW + f"No transactions found for {month_name}.\n")
        return

    grouped = {}
    for date, txn_id, time_str, amount in data:
        if date not in grouped:
            grouped[date] = []
        grouped[date].append((txn_id, time_str, amount))
    monthly_total=0

    for date, transactions in grouped.items():
        print(Fore.CYAN + f"\nDATE: {date}")
        print(tabulate(transactions, headers=["Transaction ID", "Time", "Amount"], tablefmt="grid"))
        total = sum([t[2] for t in transactions])
        monthly_total += total
        print(Fore.GREEN + f"TOTAL : {total}\n")

    print(Fore.MAGENTA+f"TOTAL OF {month_name} month: {monthly_total}\n")

def display_user():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute(f"""
        SELECT user_id, password
        FROM users
        ORDER BY user_id, password
    """)
    data = cur.fetchall()
    con.close()

    print(tabulate(data, headers=["User ID", "Password"], tablefmt="grid"))
