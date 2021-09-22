import datetime
import time
import math
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
    """
    Get the amount to deposit from the user. This needs to be a integer.
    """

    print("How much would you like to deposit")
    amount_deposit = float(input("Please enter the amount\n"))
    validate_input(amount_deposit)
    currency = "€{:,.2f}".format(amount_deposit)
    update_worksheet_deposit(currency)
    update_balance_deposit()
    calculate_current_balance()
    time.sleep(2)
    welcome()
    

def withdraw():
    print("How much would you like to withdraw")
    amount_withdrawn = float(input("Please enter the amount\n"))
    currency = "€{:,.2f}".format(amount_withdrawn)
    update_worksheet_withdraw(currency)
    update_balance_withdrawal()
    calculate_current_balance()
    time.sleep(2)
    welcome()

  
def check_balance():
    print("Your balance is blaablablabla")
    welcome()     


def validate_input(values):
    """
    Needs to check that if the value input is float and raise error if not.
    Value needs to be in xxx.xx format (left of comma can be many numbers, right of comma only two)

    """

def update_worksheet_deposit(data):

    """
    This function updates succesfull deposits to the worksheet, add new row to sheet.
    """
    x = str(datetime.datetime.now())
    print("Processing your deposit.....\n")
    deposit_worksheet = SHEET.worksheet("deposit")
    deposit_worksheet.append_row([x,data])
    time.sleep(3)
    print("Deposit succesfully processed\n.")


def update_worksheet_withdraw(data):
    """
    This function updates succesfull deposits to the worksheet, add new row to sheet.
    """
    x = str(datetime.datetime.now())
    print("Processing your withdrawal.....\n")
    withdraw_worksheet = SHEET.worksheet("withdraw")
    withdraw_worksheet.append_row([x,data])
    time.sleep(3)
    print("withdrawal succesfully processed\n Please take out your cash")


def update_worksheet_balance(calculated_balance):
    """
    This function updates the current balance to the worksheet, add new row to sheet.
    """
    x = str(datetime.datetime.now())
    balance_worksheet = SHEET.worksheet("balance")
    balance_worksheet.append_row([x,calculated_balance])


def update_balance_deposit():
    deposits = SHEET.worksheet("deposit").col_values(2)
    deposits.remove('deposit')

    for dep in range(len(deposits)):
        deposits[dep] = deposits[dep][1:]
        deposits[dep] = deposits[dep].replace(',', '')
        deposits[dep] = int(float(deposits[dep]))
    global sum_d
    sum_d = (sum(deposits))
    return sum_d
    
    

def update_balance_withdrawal():
    withdrawals = SHEET.worksheet("withdraw").col_values(2)
    withdrawals.remove('withdraw')

    for wit in range(len(withdrawals)):
        withdrawals[wit] = withdrawals[wit][1:]
        withdrawals[wit] = withdrawals[wit].replace(',', '')
        withdrawals[wit] = int(float(withdrawals[wit]))
    global sum_w
    sum_w = (sum(withdrawals))
    return sum_w
    
    
def calculate_current_balance():

    output_dep = update_balance_deposit()
    output_with = update_balance_withdrawal()
    current_balance = output_dep - output_with
    calculated_balance = "€{:,.2f}".format(current_balance)
    update_worksheet_balance(calculated_balance)
    
    

    """
    Run all the program functions

    """



def main():
    welcome()
    choice()




main()
