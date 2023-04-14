import re
def specialChecker(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #use search and find if there's at least 1 special char in string. False if can't find and True if found
    if(regex.search(string)==None):
        return False
    else:
        return True
def pwdChecker(password):
    #count and check for uppercase
    uppercase = sum(1 for char in password if char.isupper())
    print(uppercase)
    #count and check for lowercase
    lowercase = sum(1 for char in password if char.islower())
    print(lowercase)
    #count and check for number
    digit = sum (1 for char in password if char.isdigit())
    print(digit)
    #check for special char
    specialChar = specialChecker(password)
    print(specialChar)
    #if all requirement are satisfied return True, else return False
    if(uppercase>0 and lowercase>0 and digit>0 and specialChar==True):
        return True
    else:
        return False

dictionary = {"John":1,"Ana":2,"Bell":3}
for items in dictionary.items():
    print(items[0],":",items[1])
dictionary.update({"John":123})
for items in dictionary.items():
    print(items[0],":",items[1])
    