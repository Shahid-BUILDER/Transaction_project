from db_config import connect_to_db
from utilities.table_create import create_month_table, create_User_table

def add_transaction(month_name, txn_id,date_str, time_str, amount):
    con=connect_to_db()
    if con is None:
        print("Database connection failed.")
    try:
        create_month_table(month_name)
        cur=con.cursor()
        query=f"INSERT INTO `{month_name}` (transaction_id, date_entry, time_entry, amount) VALUES (%s, %s, %s, %s)"
        cur.execute(query,(txn_id,date_str, time_str, amount))
        con.commit()
        print(f"Transaction {txn_id} added to {month_name}")
    except Exception as e:
        print(f"Error adding transaction : {e}")
    finally:
        con.close()

def add_users(user_name, passw):
    con=connect_to_db()
    if con is None:
        print("Database connection failed.")
    try:
        table="users"
        create_User_table(table)
        cur=con.cursor()
        query=f"INSERT INTO `{table}` (user_id, password) VALUES (%s, %s)"
        cur.execute(query,(user_name,passw))
        con.commit()
        print(f" User {user_name} created successfully!!")
    except Exception as a:
        print(f"Error adding user {user_name}",a)
    finally:
        con.close()
