from db_config import connect_to_db
from utilities.admin import menu
from utilities.user import U_menu
from utilities.helpers import login
from utilities.user_type import choice

def con_close():
    if con:
        con.close()

if __name__ == "__main__":
    con = connect_to_db()
    a=choice()
    if a==0:
        print("Exiting.......")
        con_close()
        exit(0)
    elif a==1:
        if login(con):
            menu()
    elif a==2:
        if login(con):
            U_menu()
