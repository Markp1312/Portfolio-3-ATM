# Portfolio Project 3 - ATM Machine

## Introduction

Welcome to my ATM Machine. ATM Machine is a python based program which runs in a mock terminal on Heroku. 
The program simulates all activaties that can be done with a regular ATM Machine.
Users can Deposit money, Withdraw money and Check their balance.

---

The live version of the project can be found [here](https://www.nu.nl).

![ATM Machine Interface](assets/images/ATM%20Interface.jpg)

---
## Operation of the ATM Machine.

When opening up the program, users will be presented with 4 options.

1. Deposit

   This options enables users to deposit money.

2. Withdraw

   This option enables users to withdraw money.

3. Check Balance

   This option enables users to check their current balance

4. Exit

   This option will exit the program and "Eject the card"

---
## Features

- Input Validation
  - Users can not enter negative numbers or numbers that start with 0.
  - ATM Machine only contains numpad so validation for letters has not been implemented since these can not be entered.
  - You can not withdraw more money then your current balance. When the amount of withdrawal exceeds current balance then user is notified.

---
## Future Features

- Add the option to enter client ID and track input against this client ID.
- Add admin panel to create customer profiles and view transactions.

---
## Data Model

---
## Testing

 - Tested the code in PEP8 linter and confirmed there are no problems.
 - Given invalid input: Integers starting with 0 and Negative numbers.
 - Tested all menu options on my local machine and heroku
 - Checked that data is correctly written to Gsheet.

---

## Bugs

### Solved Bugs
- I collected the inputs as integer and converted this to a string when writing to Gsheet for readability. When pulling the data back in it had to be correctly converted back from string to int. This was tricky because I use a Euro sign (€) within the string.    

### Open Bugs
- None remaining

---
## Validator Testing
- PEP8
  - No big errors are returned.

---

## Deploymenmt

This project was deployed by using Code Institute's template for python.

- 




