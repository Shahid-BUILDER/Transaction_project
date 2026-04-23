from db_config import connect_to_db

def create_month_table(month_name):
    con=connect_to_db()
    if con is None:
        print("Failed to connect to DB while creating table.")
        return
    try:
        cur=con.cursor()
        query=f"""CREATE TABLE IF NOT EXISTS `{month_name}` (id INT AUTO_INCREMENT PRIMARY KEY, transaction_id VARCHAR(50), date_entry DATE, time_entry VARCHAR(20), amount DECIMAL(10,2))"""
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(f"Error creating table {month_name}: {e}")
    finally:
        con.close()

def create_User_table(table):
    con=connect_to_db()
    if con is None:
        print("Failed to connect to DB while creating table.")
        return
    try:
        cur=con.cursor()
        quer=f"""CREATE TABLE IF NOT EXISTS `{table}` (id INT AUTO_INCREMENT PRIMARY KEY, user_id VARCHAR(55), password VARCHAR(30))"""
        cur.execute(quer)
        con.commit()
    except Exception as e:
        print("Error creating table of users")
    finally:
        con.close()
