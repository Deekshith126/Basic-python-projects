import csv
from IPython.display import clear_output

import os
path = '...\..\' # path to save csv
os.chdir(path)

#Handling user registartion and writing to csv
def registerUser():
    with open('users.csv',mode = 'a',newline = '') as f:
        writer = csv.writer(f,delimiter = ',')
        print('Please enter your Info to register: ')
        email = input('E-mail: ')
        password = input('Password: ')
        password2 = input('Re-type password: ')
        clear_output()
        if password == password2:
            writer.writerow([email, password])
            print('You are now registered')
        else:
            print('Sorry!! something went wrong, please try again.')
			
#ask for user info and return boolean values for correct and  incorrect info
def loginUser():
    print('To login, please enter your credentials')
    email = input('E-mail: ')
    password = input('Password: ')
    clear_output()
    with open('users.csv', mode ='r') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if row == [email, password]:
                print('you are logged in')
                return True
    print('Something went wrong. Please try again')
    return False
    
#Ask for info to chnage password
def changePassword():
    print('To update password, please prove that you are you')
    email = input('E-mail: ')
    password = input('Old Password: ')
    password1 = input('New Password: ')
    clear_output()
    with open('users.csv', mode ='r') as f:
        r = csv.reader(f)
        lines = list(r)
        for row in lines:
            if row[0]==email:
                row[1]=password1
                writer = csv.writer(open('users.csv', 'w'))
                writer.writerows(lines)
                print('password changed Succefully')
                return True
            elif password == password1:
                print('same password cannot be updated')
                return False
            else:
                print('Something went wrong please try again')
                return False
	
#Run the whole program through main looo
active = True
logged_in = False
# main loop
while active:
    if logged_in:
        print('1. change password\n2. Logout\n3. Quit')
    else:
        print('1. Register\n2. Login\n3. Logout\n4. Quit')
    choice = input('Continue through your choice: ').lower()
    clear_output()
    if choice =='register' and logged_in== False:
        registerUser()
    elif choice =='login' and logged_in == False:
        logged_in = loginUser()
    elif choice =='quit':
        active = False
        print('Thanks for using program')
    elif choice =='change password' and logged_in == True:
        changePassword()
    elif choice =='logout' and logged_in == True:
        logged_in = False
        print('You are logged out')
    else:
        print('sorry try again')