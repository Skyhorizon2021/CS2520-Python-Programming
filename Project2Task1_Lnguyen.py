#Name: Loc Nguyen
#Project 1 Task 1
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
    lengthOfStr = len(inputStr)
    return lengthOfStr

def output_without_whitespace(inputStr):
    lengthOfStrNoSpace = len(inputStr) - inputStr.count(' ')
    return lengthOfStrNoSpace

def get_safe(plaintext):
    return encryptedMsg

def go_recover(encryptedMsg):
    return plaintext

def main():

    return 

main()



