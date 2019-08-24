"""
Here we have some transaction function
in which we have 
deposit & withdrwal money
check balance and password updation facilities
"""
import os
import time
import shelve
from getpass import getpass
from log import update_log
def debit():
    print("\n\t")
    db=shelve.open('database/bank.db',writeback=True)
    acc=input("enter account number: ")
    curr_bal = db[acc]['bal']
    amt=int(input("Enter amount which you want to withdrawl: "))
    if amt > curr_bal:
        update_log("ERROR",f"Deny for withdrwal for acc no {acc}")
        print("\nInsufficient Balance")
    else:
        print("\n\tYour Previous Balance is",curr_bal)
        new_bal=curr_bal-amt
        db[acc]['bal']=new_bal
        print("\n\tYour Updated balance is",new_bal) 
        update_log("INFO",f"Withdrawl Successful")
    db.close()
def credit():
    db=shelve.open('database/bank.db',writeback=True)
    acc=input("enter account number: ")
    CB = db[acc]['bal']
    amt=int(input("\n\tEnter amount which you want to deposit: "))
    print("Your Previous Balance is",CB)
    NB=CB+amt
    db[acc]['bal']=NB
    print("\n\tYour Updated balance is",NB)
    update_log("INFO",f"Amount Deposit Successful")
    db.close()
def check_bal():
    db=shelve.open('database/bank.db',writeback=True)
    acc=input("enter account number: ")
    CB=db[acc]['bal']
    update_log("INFO",f"Checking for balance")
    print("\n\tYour account balance is :",CB)
    db.close()
def update_pwd():
    db=shelve.open('database/bank.db',writeback=True)
    acc=input("enter account number: ")
    p1=getpass("enter new password :")
    p2=getpass("re-type password :")
    if p1==p2:
        db[acc]['password'] = p1
        update_log("INFO","Password Update")
        print("\n")
        print(f"Password updated successfully for account number {acc}")
    else:
        update_log("ERROR","Invalid Input")
        print("\n\tplease enter valid input")
        update_pwd()
    db.close()
            