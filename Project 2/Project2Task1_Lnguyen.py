#Name: Loc Nguyen
#Project 2 Task 1
'''Objective: Text analyzer & modifier using functions
(1) Complete the get_num_of_characters() function, which takes a string as parameter and returns the number of 
characters in the user's string. We encourage you to use a for loop in this function.   
(2) Implement the output_without_whitespace() function. output_without_whitespace() takes a string as 
parameter and returns the string's characters except for whitespace (spaces, tabs). Note: a tab is '\t'. 
(3) Write a function get_safe() that takes a string as parameter and encrypts it using an encryption method of 
your choice. It returns the encrypted message.
(4) Write a function go_recover() that takes a string as parameter and decrypts it (according to the encryption 
method you used above). It returns the decrypted message. 
(5) Create a main() function that first prompts the user to enter a sentence of their choice, print out the string, 
the calls functions in (1) to (4) respectively, printing out the result after each function call.
(6) call the main function to test run the program. You must run the test case provided plus additional two 
different test runs. Note: a call to main function is a must.'''

def get_num_of_characters(inputStr):
    lengthOfStr = 0
    for char in inputStr:
        lengthOfStr+=1
    return lengthOfStr

def output_without_whitespace(inputStr):
    #lengthOfStrNoSpace = len(inputStr) - inputStr.count(' ')
    StrNoSpace=inputStr.replace(" ","")
    print("String with no whitespace is",StrNoSpace)
    lengthOfStrNoSpace=get_num_of_characters(StrNoSpace)
    return lengthOfStrNoSpace

def vignereEncrypt ():
    #get desired key and plaintext
    key=input("Please enter the encryption key: ")
    plaintext=input("Please enter the plaintext: ")
    #lowercase all key and plaintext
    plaintext=plaintext.lower()
    key=key.lower()
    #remove whitespace
    plaintext=plaintext.replace(' ','')
    #get length of key and initialize empty string to store ciphertext
    keyLength=len(key)
    cipherText=''
    #loop through the length of plaintext char by char and use mod 
    #to find proper index of key char to encrypt with
    for i in range(len(plaintext)):
        letter = plaintext[i]
        k = key[i % keyLength]
        cipherText = cipherText + chr(((ord(letter) - 97) + (ord(k)-97)) % 26 + 97)
    print("Encrypted text is:",cipherText)
    return cipherText,key

def go_recover():
    ciphertext,key=vignereEncrypt()
    keyLength=len(key)
    plaintext=''

    for i in range(len(ciphertext)):
        letter=ciphertext[i]
        k = key[i % keyLength]
        plaintext = plaintext + chr(((ord(letter)-97) - (ord(k)-97)) %26 + 97)
    print("Plaintext is:",plaintext)
    return plaintext

def main():
    inputStr = input("Enter a string: ")
    print("You entered",inputStr)
    print("Number of characters:",get_num_of_characters(inputStr))
    print("Number of characters:",output_without_whitespace(inputStr))
    go_recover()
     

main()
'''Output
Test(1)
Enter a string: The only thing we have to fear is fear itself
You entered The only thing we have to fear is fear itself
Number of characters: 45
String with no whitespace is Theonlythingwehavetofearisfearitself
Number of characters: 36
Please enter the encryption key: Megafear is contagious
Please enter the plaintext: The only thing we have to fear is fear itself
Encrypted text is: flkospykuqftysutvkbczwmvoskiaivbkrnt
Plaintext is: theonlythingwehavetofearisfearitself
Test(2)
Enter a string: How many times you fail matter more than how much you succeed
You entered How many times you fail matter more than how much you succeed
Number of characters: 61
String with no whitespace is Howmanytimesyoufailmattermorethanhowmuchyousucceed    
Number of characters: 50
Please enter the encryption key: Python
Please enter the plaintext: Data Science is important   
Encrypted text is: symhgpxcgjsvhgfwceiyga
Plaintext is: datascienceisimportant
Test(3)
Enter a string: John is hungry
You entered John is hungry
Number of characters: 14
String with no whitespace is Johnishungry
Number of characters: 12
Please enter the encryption key: Hello World
Please enter the plaintext: John is not hungry
Encrypted text is: qssywfjcksxukcj
Plaintext is: johnisnothungry'''

