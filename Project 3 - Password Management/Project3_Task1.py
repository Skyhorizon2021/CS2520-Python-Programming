#Name: Loc Nguyen
#Date: 04/13/2023
'''Objective: 
main() function:
1. Create two lists (you choose how to enter/initialize these two lists) usernames and passwords,
e.g. usernames = ['lyang', 'kSimon', 'danny', ...], passwords = ['sheCodes#123',
'catchAllGood1%', '@my2Choices', ...]. The usernames and passwords must meet the following
requirements: Usernames must contain letters (lowercase as well as uppercases can be used).
Usernames are unique (i.e. no two usernames can be the same.) Passwords must meet the
following requirements: (1) at least 8 characters, (2) contains at least one lowercase letter, one
uppercase letter, one digit, and one special character (non-letter or digit). We assume the
usernames and passwords in the initialized lists have met the requirements (your responsibility
to ensure that.)
2. Zip two lists to form a dictionary of usernames/passwords with the username as the key.
3. Call functions (see below) to perform: (1) login users; acknowledge if login successful or not. (2)
change passwords; acknowledge if password change successful or not. (3) create new user; if
successful, welcome the new user. If not, acknowledge it.
The following functions are needed:
1. A function to authenticate/login a user, i.e. it takes the dictionary as a parameter, prompts for a
username, if username not exist, issue error message, but do allow 3 attempts before the
function returns False (unsuccessful). If the username is found, asks for a password. Login the
user if password matches, allow 3 tries. If successful, the function returns a Boolean value True.
2. A function to create a new user. Again, the function should take the dictionary as parameter,
prompts for a username (verify the username meets the above requirements, i.e. in valid format
and not duplicate with existing one) and then a password (verify that the password meets the
above requirements). If one of them not valid (okay for one attempt only, but you may design
multiple attempts if you wish - optional) the function returns a None value, if both the
username and passwords are valid, the function returns the username (so that in main()
function, you could acknowledge, welcome ....).
3. A function to update the password. Again, it takes the dictionary as the parameter. Its asks for
the username and password of the existing user, login first. If login successful, asks for new
password, verify that the password meets the requirement, and updates it, then the function
terminates by returning a True value. If any issue (i.e. can't login or new password doesn't meet
the requirements etc.) the function terminates by returning a False value without updating the
dictionary.
Required test run: one test run that covers all (primary) features described above. Initialize the
username and password lists as follows, then try to login a user, add a new user, and update password.
In each action (login/add/update) try both scenarios (i.e. successful or unsuccessful).
usernames = ['lyang', 'kSimon', 'danny', 'tomatcpp', 'csDept', 'CoScpp', 'broncoWins', 'ponyExp',
'BldgAndRooms', 'helloKitty' ] #note: you may use different usernames, but make sure all are valid.
passwords = ['sheCodes#123', 'catchAllGood1%', '@my2Choices', '123abc;;;', 'Hello2Monday$',
'GoodFriday@Cpp2', 'CS2520@Python', 'JavaIsHot2!', '2ManyRainingDays!', '1Startup@Starbucks']
#note: you may use different passwords, but make sure all are valid.'''

#import typing to restrict what type of parameter to pass to function/method
from typing import Dict
import re
#function to check for special characters using regex
def specialChecker(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #use search and find if there's at least 1 special char in string. False if can't find and True if found
    if(regex.search(string)==None):
        return False
    else:
        return True
def pwdChecker(password):
    #check for length at least 8 char
    length = len(password)
    #count and check for uppercase
    uppercase = sum(1 for char in password if char.isupper())
    #count and check for lowercase
    lowercase = sum(1 for char in password if char.islower())
    #count and check for number
    digit = sum (1 for char in password if char.isdigit())
    #check for special char
    specialChar = specialChecker(password)
    #if all requirement are satisfied return True, else return False
    if(length>=8 and uppercase>0 and lowercase>0 and digit>0 and specialChar==True):
        return True
    else:
        return False
#function to log user in
def authenticate(loginDict :Dict):
    print("Log in below")
    #allow 3 tries
    counter = 0
    while counter<3:
        global usernameInput
        usernameInput = input("Please enter your username: ")
        #if usrname is in dict as key, prompt password
        if usernameInput in loginDict.keys():
            #allow 3 tries
            counter = 0
            #access dictionary using key to get password to compare later
            realPwd = loginDict[usernameInput]
            while counter<3:
                pwdInput = input("Please enter your password: ")
                if pwdInput == realPwd:
                    print("Login Successful!")
                    
                    return True
                else:
                    counter +=1
        else:
            counter+=1
    else:
        return False
    
#function to create username and password with specification
def newUser(loginDict:Dict):
    print("Create a new user below")
    usernameInput = input("Please create your username: ")
    #check for unique username and prompt reenter if not unique
    while(usernameInput==loginDict.keys()):
        usernameInput = input("Username already existed.\nPlease create your username: ")
    else:
        pwdInput = input("Please create your password: ")
        #while the pwdChecker return False meaning password doesn't meet requirement, the loop is True and will continue to run until requirement is met 
        #so pwdChecker return True and "not True" = False will terminate the loop
        while not(pwdChecker(pwdInput)):
            pwdInput = input("Password complexity requirement not met. Length of at least 8, 1 lowercase, 1 uppercase, 1 digit, and 1 special character\nPlease create your password: ")
        else:
            print("Account Creation successful!")
            loginDict.update({usernameInput:pwdInput})   
    return usernameInput
#function to update password
def updatePwd(loginDict:Dict):
    print("Update your password below. Please log in first")
    if authenticate(loginDict) == True:
        pwdInput = input("Please update your password: ")
        #while the pwdChecker return False meaning password doesn't meet requirement, the loop is True and will continue to run until requirement is met 
        #so pwdChecker return True and "not True" = False will terminate the loop
        while not(pwdChecker(pwdInput)):
            pwdInput = input("Password complexity requirement not met. Length of at least 8, 1 lowercase, 1 uppercase, 1 digit, and 1 special character\nPlease update your password: ")
        else:
            print("Password Update Successful for User",usernameInput)
            loginDict.update({usernameInput:pwdInput})
            return True
    else:
        return False


def main():
    #initialize user and password list
    userList = ['lyang', 'kSimon', 'danny', 'tomatcpp', 'csDept', 'CoScpp', 'broncoWins', 'ponyExp','BldgAndRooms', 'helloKitty' ]
    pwdList = ['sheCodes#123', 'catchAllGood1%', '@my2Choices', '123abc;;;', 'Hello2Monday$','GoodFriday@Cpp2', 'CS2520@Python', 'JavaIsHot2!', '2ManyRainingDays!', '1Startup@Starbucks']
    #zip the 2 list and cast it to be a Dictionary type
    loginDict = dict(zip(userList,pwdList))
    '''for items in loginDict.items():
        print(items[0],":",items[1])'''
        
    #prompt user login & print corresponding status update
    if authenticate(loginDict) == True:
        pass
    else:
        print("Login Unsuccessful!")
    
    #create a new user, if account creation is successful, it will return the username. We'll check if the username is in the dictionary, if it is, welcome the user
    newUsername = newUser(loginDict)
    if(newUsername in loginDict.keys()):
        print("Welcome",newUsername+"!")
    #update password
    if updatePwd(loginDict) == False:
        print("Password update unsuccessful. End of program!")
#execute main function
main()
'''Output
Test(1) - Successful login, create account, and update password
Log in below
Please enter your username: iwant
Please enter your username: youtube
Please enter your username: helloKitty
Please enter your password: 1Startup@sdlfaksdjf
Please enter your password: 1Startup@Starbucks
Login Successful!
Create a new user below      
Please create your username: Analys
Please create your password: opening
Password complexity requirement not met. Length of at least 8, 1 lowercase, 1 uppercase, 1 digit, and 1 special character
Please create your password: Urthebest263
Password complexity requirement not met. Length of at least 8, 1 lowercase, 1 uppercase, 1 digit, and 1 special character
Please create your password: Getthebag78@
Account Creation successful!
Welcome Analys!
Update your password below. Please log in first
Log in below
Please enter your username: tomatcpp
Please enter your password: John
Please enter your password: 123abc;;;
Login Successful!
Please update your password: 4Begone123!
Password Update Successful for User tomatcpp
Test(2) - Unsuccessful login, succesful create account, unsuccessful password update
Log in below
Please enter your username: Analys
Please enter your username: ponyExp
Please enter your password: Johnl
Please enter your password: I can't take it
Please enter your password: python
Login Unsuccessful!
Create a new user below
Please create your username: user
Please create your password: user
Password complexity requirement not met. Length of at least 8, 1 lowercase, 1 uppercase, 1 digit, and 1 special character
Please create your password: I want to be 11
Password complexity requirement not met. Length of at least 8, 1 lowercase, 1 uppercase, 1 digit, and 1 special character
Please create your password: Python2520!
Account Creation successful!
Welcome user!
Update your password below. Please log in first
Log in below
Please enter your username: Ucla
Please enter your username: Cpp
Please enter your username: Get me a 
Password update unsuccessful. End of program!
'''
