from datetime import datetime

name = input('What is your name? \n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if (name in allowedUsers):
    password =  input('Your password: \n')
    userID = allowedUsers.index(name)

    if(password == allowedPassword[userID]):
        balance = 0
        done = False
        while done == False:
            print('Welcome %s' % name)
            now = datetime.now()
            print('The current date and time is:', now)
            print('Your current balance is: $', balance)
            print('These are the available options:')
            print('1. Withdraw')
            print('2. Desposit')
            print('3. Complaint')
            print('4. Exit')

            selectedOption = input('Please select an option: ')

            if(selectedOption == '1'):
                print('You selected %s' % selectedOption)
                withdraw = int(input('How much do you want to withdraw? \n'))
                print("Here's your cash: $%s \n" % withdraw)
                balance = balance - withdraw
            elif(selectedOption == '2'):
                print('You selected %s' % selectedOption)
                deposit = int(input("How much would you like to deposit? \n"))
                balance = balance + deposit
                print('Current balance is %s \n' % balance)
            elif(selectedOption == '3'):
                print('You selected %s' % selectedOption)
                complaint = input("What issue will you report? \n")
                print("Thank you for contacting us. \n")
            elif(selectedOption == '4'):
                print('Thank you!')
                done = True
            else:
                print('Invalid option selected, please try again. \n')

    else:
        print('Password incorrect, please try again!')
        
else:
    print('Name not found, please try again!') 
