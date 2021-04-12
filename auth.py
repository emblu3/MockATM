import random 
database = {}

def init():
    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if haveAccount == 1:
        login()

    elif haveAccount == 2:
        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("--- LOGIN ---")

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bank_operation(userDetails)

    print('Invalid account or password')
    init()


def register():
    print("--- REGISTER ---")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    account_number = generate_account_number()
    balance = 0

    database[account_number] = [first_name, last_name, email, password, balance]

    print("Your account Has been created! \n")
    print("Your account number is: %d \n" % account_number)
    print("Make sure you keep it safe. \n")

    login()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdraw (3) Logout (4) Exit \n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        logout()

    elif selected_option == 4:
        exit()

    else:
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    print("You selected: Withdrawal")
    print('Your current balance is %s' % user[4])
    withdraw = int(input('How much do you want to withdraw? \n'))
    if user[4] > withdraw:
        print("Here's your cash: $%s \n" % withdraw)
        user[4] = user[4] - withdraw
        print("Your new balance is %s" % user[4])
    else:
        print("You don't have enough money to withdraw that amount. \n")
    
    bank_operation(user)


def deposit_operation(user):
    print("You selected: Deposit")
    print('Your current balance is %s' % user[4])
    deposit = int(input('How much do you want to deposit? \n'))
    user[4] = user[4] + deposit
    print('Your new balance is %s' % user[4])
    
    bank_operation(user)


def generate_account_number():
    return random.randrange(1111111111, 9999999999)



def logout():
    login()


init()