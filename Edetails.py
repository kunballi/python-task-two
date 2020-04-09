#import libraries
import string
import random

#getting user users_details
def get_details():
    first_name=input('Enter your first name: ')
    last_name=input('Enter your last name: ')
    user_email=input('Enter your email address: ')
    details=[first_name,last_name,user_email]

    return details

#random password generated using user get_details
def gen_password(details):
    characters=string.ascii_letters
    lenght=5
    random_password=''.join(random.choice(characters)for i in range(lenght))
    password=str(details[0][0:2]+details[1][-2:]+random_password)

    return password

#main project
container=[]
users={}
user_count=1

while True:
    #getting user details
    details=get_details()
    #showing generated Password
    password=gen_password(details)
    print('Your password is: ',str(password))

    #asking if the password is good to continue
    password_ok=input(str('Do you like the password.If yes enter YES and if no, enter NO ')).upper()
    while True:
        if password_ok=='YES':
            #adding password to user get_details
            details.append(password)
            #compiling user details to the container
            container.append(details)
            users[user_count]=details
            break
        elif password_ok=='NO':
            user_password=input(str('Create your own password longer or equal to 7: '))
            #checking password lenght
            while True:
                if len(user_password)>=7:
                    details.append(user_password)
                    container.append(details)
                    users[user_count]=details
                    break
                else:
                    print('your password is less than 7')
                    user_password=input('Enter password longer than or equal to 7: ')
            break
        else:
            print('invalid input')
            password_ok=input(str('Enter Yes or No  ')).upper()
    #new user
    new_user=input(str('Would you like to enter a new user? Yes or No ')).upper()
    if new_user=='YES':
        user_count=user_count+1
    elif new_user=='NO':
        for item in users:
            print(item,users[item])
        break