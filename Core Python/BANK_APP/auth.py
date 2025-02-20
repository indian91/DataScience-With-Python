"""
 Here we use some authenication functions like 
 login and signup
"""
import os
import time
import shelve
import getpass
from menu import sub_menu
from log import update_log

def login():
    acc = input("\n\n\t\tEnter account number :) ")
    db = shelve.open("database/bank.db")
    if acc in db.keys() : 
        password = getpass.getpass("\n\t\tPassword :) ")
        if password == db[acc]['password'] : 
            update_log("LOGIN",f"Login sucessfull for acc no {acc}")
            print("Welcome to our Bank")
            sub_menu()
        else : 
            update_log("ERROR",f"Login unsucessfull for acc no {acc} because of Password Verification")
            print("\n\n\t\tError!! Invalid Password....Try Again")
            login()
                
    else : 
        update_log("DENY","unauthoriged account accessed")
        print("\n\n\t\tError!!! Invalid Account Number")
        print("\n\n\t\tIf you are a new user please SignUp First")
        login()

def signup():
    os.system("cls")
    print("\n\n\t\tWelcome to Signup Service\n\n")
    print(f"Time : {time.ctime()}")
    name = input("\n\n\tEnter your name : ")
    bal = eval(input("\n\tEnter your initial amount : "))
    password = getpass.getpass("\n\tPassword :")
    db = shelve.open('database/bank.db',writeback=True)
    acc_no = db.get('last_acc') + 1
    db['last_acc'] = acc_no
    acc_no = str(acc_no)
    db[acc_no] = { 'name':name,'bal':bal,'password':password } 
    db.close()
    update_log("SIGNUP",f"Signup sucessfull for acc no {acc_no} because of Password Verification")
    print("\n\n\tAccount Create Sucessfully Write down your account number ")
    print(f"\n\n\t your account num is {acc_no} and used to login \n\n")
    input("\n\n...........Press any key to continue....")
