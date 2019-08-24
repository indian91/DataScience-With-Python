"""This is the sub menu 
which contain the transaction functions.
"""
import os
import time
import shelve
import getpass
from transaction import credit,debit,update_pwd,check_bal
from log import update_log
def sub_menu():
    time.sleep(2)
    os.system('cls')
    s = """
        1. Credit
        2. Debit
        3. Update_pwd
        4. Check Balance
        5. Logout
    """
    print(s)
    ch=int(input("Enter the choice: "))
    if ch == 1:
        credit()
        sub_menu()
    elif ch == 2:
        debit()
        sub_menu()
    elif ch == 3:
        update_pwd()
        sub_menu()
    elif ch == 4:
        check_bal()
        sub_menu()
    