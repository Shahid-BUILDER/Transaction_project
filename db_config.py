import pymysql
from pymysql.err import MySQLError

def create_database(d_name):
    try:
        con=pymysql.connect(host='localhost', user='txn_user', password='Shahid!789')
        cur=con.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {d_name}")
        con.commit()
        #print(f"Databse {DB_NAME} ensured.")
    except MySQLError as e:
        print(f"Error creating database: {e}")
    finally:
        con.close()
def connect_to_db():
    DB_NAME="transaction_db".strip().lower()
    create_database(DB_NAME)
    try:
        con=pymysql.connect(host="localhost", user="txn_user", password="Shahid!789",database=DB_NAME)
        return con
    except MySQLError as e:
        print(f"Error connecting to database:",e)
        return None