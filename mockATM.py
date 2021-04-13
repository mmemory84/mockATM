import random
import os
import sys
import datetime
now = datetime.datetime.now()
account_balance = float(1000)

database = {}
#creating a new account  (name,email, and password)

def init():

   
    print('Welcome to bankMoney')
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

    haveAccount = int(input('Do you have an account wuith us: 1 (yes) 2 (no) \n'))

    if (haveAccount == 1):
          
          login()
    elif(haveAccount == 2):
        register()

    else:
        print('You have selected invalid option')
        init()


def login():

    print('************ Login *************')

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password \n')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

#bankoperations
    print('Welcome %s' % name)
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print('these are the variable options:')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Balance')
    print('4. logout')
    print('5. Exit')            

def register():

    print('****** Register *******')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('create a password for yourself \n')

    accountNumber = genarationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password]

    print (' Your Account Has been created')
    print(' == ==== ====== ===== ===')
    print('Your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print(' == ==== ====== ===== ===')

    login()

def bankOperation(user):
    print(' Welcome %s %s ' % (user[0], user[1] ) )

    selectedOption = int(input('What would you like to do? (1) deposit (2) withdrawal (3) balance (4) logout (5) Exit \n'))

    if(selectedOption == 1):
        deposit()

    elif(selectedOption == 2):
        withdrawal()

    elif(selectedOption == 3):
        account()

    elif(selectedOption == 4):
        logout()

    elif(selectedOption == 5):
        exit()
    else:
        print('invalid option selected')  
        bankOperation (user)  
account_balance = float(1000)


def account_balance():

    print( "Your current balance: $%.2f"%account_balance)


def deposit_amount():
    global balance

    account_balance=account_balance+deposit_amount

    print("Deposit was $%.2f, current balance is $%.2f"%(deposit_amount,account_balance))


def withdrawal_amount():

    global account_balance

    if(withdrawal_amount>account_balance):

        print ("withdrawal_amount is greater that your account balance of account_balance")

    else:

        account_balance=account_balance-withdrawal_amount

        print ("Deposit was $%.2f, current balance is $%.2f"%(withdrawal_amount,account_balance)) 

def genarationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

init()     
