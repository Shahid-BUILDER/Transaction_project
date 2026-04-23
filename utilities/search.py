from db_config import connect_to_db
from tabulate import tabulate

def search_transaction(month_name, txn_id):
    con=connect_to_db()
    cur=con.cursor()
    query=f"SELECT transaction_id, date_entry, time_entry, amount FROM `{month_name}` WHERE transaction_id=%s"
    cur.execute(query,(txn_id,))
    data=cur.fetchall()
    con.close()

    if data:
        print(tabulate(data, headers=["Transaction ID", "Date", "Time", "Amount"], tablefmt="grid"))
    else:
        print(f"Transaction {txn_id} not found in {month_name}")

def search_user(user, txn_id):
    con=connect_to_db()
    cur=con.cursor()
    query=f"SELECT user_id, password FROM `{user}` WHERE user_id=%s"
    cur.execute(query,(txn_id,))
    data=cur.fetchall()
    con.close()

    if data:
        print(tabulate(data, headers=["user_id","password"], tablefmt="grid"))
    else:
        print(f"User {txn_id} not found in {user}")