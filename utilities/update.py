from db_config import connect_to_db

def update_transaction(month_name, txn_id,new_date=None, new_time=None, new_amount=None):
    con=connect_to_db()
    cur=con.cursor()
    if new_date:
        cur.execute(f"UPDATE `{month_name}` SET date_entry=%s WHERE transaction_id=%s", (new_date,txn_id))
    if new_time:
        cur.execute(f"UPDATE `{month_name}` SET time_entry=%s WHERE transaction_id=%s",(new_time,txn_id))
    if new_amount:
        cur.execute(f"UPDATE `{month_name}` SET amount=%s WHERE transaction_id=%s", (new_amount, txn_id))
    con.commit()
    con.close()
    print(f"Transaction {txn_id} updated in {month_name}")