import datetime
import gspread
from google.oauth2.service_account import Credentials


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
    menu = int(input(" 1. Deposit\n 2. Withdraw\n 3. Check Balance\n 4. Exit\n"))
    while True:
        if (menu == 1):
            deposit()
            break
        elif (menu == 2):
            withdraw()
            break
        elif (menu == 3):
            print("Check Balance")
            break
        elif (menu == 4):
            print("Exit")
            print("Please take out your card")
            break
        else:
            print("This option is incorrect, please enter a valid option")
            choice()
            break  


def deposit():
    print("How much would you like to deposit")
    amount_deposit = float(input("Please enter the amount\n"))
    welcome()


def withdraw():
    print("How much would you like to withdraw")
    amount_withdrawn = float(input("Please enter the amount\n"))
    welcome()


def check_balance():
    print("Your balance is blaablablabla")
    welcome()     


"""
Run all the program functions

"""


def main():
    welcome()
    choice()


main()
