import gspread
from google.oauth2.service_account import Credentials

import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ATM_Machine')


def welcome():
    x = datetime.datetime.now()
    print(x)
    print("Welcome to Mark Financial Services")
    print("Please make one of the following options")


def choice():
    menu = int(input(" 1. Withdraw\n 2. Deposit\n 3. Check Balance\n 4. Exit"))
    while True:
        if (menu == 1):
            print("withdraw")
            break
        elif (menu ==2):
            print("Deposit")
            break
        elif (menu == 3):
            print("Check Balance")
            break
        elif (menu == 4):
            print("Exit")
            break
        else:
            print("This option is incorrect, please enter a valid option")  
            break             

"""
Run all the program functions

"""

def main():
    welcome()
    choice()

main()
