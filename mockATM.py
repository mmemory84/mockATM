import random
import os
import sys
import datetime

now = datetime.datetime.now()
account_balance = float(1000)

database = {}

def init():
    print('Welcome to bankMoney')
    print("Current date and time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    haveAccount = int(input('Do you have an account with us? 1 (yes) 2 (no)\n'))

    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print('You have selected an invalid option')
        init()

def login():
    print('************ Login *************')

    accountNumberFromUser = int(input('What is your account number?\n'))
    password = input('What is your password?\n')

    user_details = database.get(accountNumberFromUser)

    if user_details and user_details[3] == password:
        bankOperation(user_details)
    else:
        print('Invalid account number or password')
        init()

def register():
    print('****** Register *******')
    email = input('What is your email address?\n')
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    password = input('Create a password for yourself\n')

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your Account Has been created')
    print(' == ==== ====== ===== ===')
    print('Your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print(' == ==== ====== ===== ===')

    login()

def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    print("Current date and time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    print('These are the available options:')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Balance')
    print('4. Logout')
    print('5. Exit')

    selectedOption = int(input('What would you like to do?\n'))

    if selectedOption == 1:
        deposit(user)
    elif selectedOption == 2:
        withdrawal(user)
    elif selectedOption == 3:
        account_balance(user)
    elif selectedOption == 4:
        logout()
    elif selectedOption == 5:
        sys.exit()
    else:
        print('Invalid option selected')
        bankOperation(user)

def account_balance(user):
    print("Your current balance: $%.2f" % account_balance)

def deposit(user):
    deposit_amount = float(input("Enter the amount to deposit:\n"))
    global account_balance
    account_balance += deposit_amount
    print("Deposit was $%.2f, current balance is $%.2f" % (deposit_amount, account_balance))

def withdrawal(user):
    withdrawal_amount = float(input("Enter the amount to withdraw:\n"))
    global account_balance
    if withdrawal_amount > account_balance:
        print("Withdrawal amount is greater than your account balance")
    else:
        account_balance -= withdrawal_amount
        print("Withdrawal was $%.2f, current balance is $%.2f" % (withdrawal_amount, account_balance))

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout():
    init()

init()
   
