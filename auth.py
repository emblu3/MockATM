import random
import validation 
import database
from getpass import getpass

def init():
    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if haveAccount == 1:
        login()

    elif haveAccount == 2:
        register()

    else:
        print("You have selected an invalid option")
        init()


def login():
    print("\n--- LOGIN ---")

    account_number_from_user = int(input('What is your account number? \n'))
    is_valid_account_number = validation.account_number_validation(account_number_from_user) 
    
    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user, account_number_from_user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers.")
        init()
    
    


def register():
    print("\n--- REGISTER ---")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user, account_number_from_user):
    database.logged('on', account_number_from_user)

    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdraw (3) Logout (4) Exit \n"))

    if selected_option == 1:
        deposit_operation(user, account_number_from_user)

    elif selected_option == 2:
        withdrawal_operation(user, account_number_from_user)

    elif selected_option == 3:
        logout(account_number_from_user)

    elif selected_option == 4:
        database.logged('off', account_number_from_user)
        exit()

    else:
        print("Invalid option selected")
        bank_operation(user, account_number_from_user)


def withdrawal_operation(user, account_number_from_user):
    print("You selected: Withdrawal")
    print('Your current balance is %s' % user[4])
    database.update_withdrawal(user, account_number_from_user)
    
    bank_operation(user, account_number_from_user)


def deposit_operation(user, account_number_from_user):
    print("You selected: Deposit")
    print('Your current balance is %s' % user[4])
    database.update_deposit(user, account_number_from_user)
    
    
    bank_operation(user, account_number_from_user)


def generate_account_number():
    return random.randrange(1111111111, 9999999999)



def logout(account_number_from_user):
    database.logged('off', account_number_from_user)
    login()


init() 