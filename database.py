import os
import validation
import datetime

user_db_path = "data/user_record/"
user_session_path = 'data/auth_session/'

def logged(state, user_account_number):
    if state == 'on':
        try:
            f = open(user_session_path + str(user_account_number) + ".txt", "w")

        except FileExistsError: 
            does_file_contain_data = read(user_session_path + str(user_account_number) + ".txt")
            if not does_file_contain_data:
                delete_session(user_account_number)

        else:
            f.write(str("User has logged in at " + str(datetime.datetime.now())))

        finally:
            f.close()
    if state == 'off':
        try:
            delete_session(user_account_number)
        except:
            print('Session was not deleted')

def create(user_account_number, first_name, last_name, email, password):

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(user_account_number):
        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError: 
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)

    else:
        f.write(str(user_data))
        completion_state = True

    finally:
        f.close()
        return completion_state


def read(user_account_number):
    
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else: 
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found.")

    except FileExistsError:

        print("User already exists")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False

    
def update_deposit(user, account_number_from_user):

    f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
    try:
        deposit = int(input('How much do you want to deposit? \n'))
        user[4] = str(int(user[4]) + deposit)
    except:
        print('Please enter an integer.\n')
    else:
        print('Your new balance is %s' % user[4])
    finally:
        user = ",".join(user)
        f.write(str(user))

def update_withdrawal(user, account_number_from_user):

    f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
    try:
        withdraw = int(input('How much do you want to withdraw? \n'))
        current_amount = int(user[4])
        if current_amount > withdraw:
            print("Here's your cash: $%s \n" % withdraw)
            user[4] = str(current_amount - withdraw)
        else:
            print("You don't have enough money to withdraw that amount. \n")
    except:
        print('Please enter an integer.\n')
    else:
        print('Your new balance is %s' % user[4])
    finally:
        user = ",".join(user)
        f.write(str(user))


def delete_session(user_account_number):

    is_delete_successful = False

    if os.path.exists(user_session_path + str(user_account_number) + ".txt"):

        try:
            os.remove(user_session_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:
            print("User not found")

        finally:
            return is_delete_successful


def delete(user_account_number):

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:
            print("User not found")

        finally:
            return is_delete_successful


def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user == str(account_number) + ".txt":
            return True

    return False


def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False