"""
documentation string of bank application

this is a simple bank application having some
basic functionalities such as 
    debit
    credit
    check_bal
    update password

"""
import os
import time
import random 
import shelve
from menu import sub_menu
from auth import login, signup
from log import update_log


def main_menu():
    
    update_log("InFO","Application Started") 
    os.system("cls")
    print("\n\n")
    print(f"\n\t\t {time.ctime()} Welcome User ")
    s = """
        1. Login
        2. Signup
        3. Exit
    """
    print(s)
    while True :
        try : 
            print('\n')
            ch = int(input("Enter your choice : ".rjust(30)))
            if ch < 1 or ch > 3 : 
                print("\n\n\t\tError!!! Invalid Choice")
                continue
            break
        except ValueError as e : 
            print("\n\n\t\tError!!!Bhaai saab integer choice string mtt do")

    if ch == 1 :
        update_log("INFO","User Tried To Login")
        login()
    elif ch == 2 : 
        update_log("INFO","User Tried To Signup")
        signup()
        main_menu()



if __name__ == "__main__" : 
    
    main_menu()
    os.system('cls')
    print("\n\n\n")
    print("\t\t\tThanks for using Our Services")
    print("\n\n\t\t..................Exiting.............")
    update_log("INFO","Application Closed")
    time.sleep(random.randint(2,5))
    os.system('cls')

