#Name: Loc Nguyen
#Date: 3/24/2023
'''Objective: Create a list of words from a paragraph of text, e.g. python is an easy language python is easy to
learn and easy to code a lot of python modules that are easy to use go python (note: here
punctuation or other special characters are omitted in the input, but as we discussed in the
lecture, you may write code to remove these non-alphabet characters. You decide which way to
go.)
(2) Create a dictionary to store words (as key) and the corresponding frequencies (as value). Print
out the content of the dictionary with each line a word and its frequency.
(3) Display the top 3 most frequent words (as well as the corresponding frequencies) stored in the
dictionary.
(4) Test your code with the above given text (e.g. python is an easy ....), then run two additional
tests with your own input (make sure your input paragraph having at least 50 words, or 2+ lines
long.)'''

from collections import *
#function to remove nonalphabetic characters
def removeNonAlpha(inputStr):
    i = 0
    while i < len(inputStr):
        #Find characters that doesn't fall within ASCII alphabetic range
        if(ord(inputStr[i])<ord('A') or ord(inputStr[i])>ord('Z') or ord(inputStr[i])<ord('a') or ord(inputStr[i])>ord('z')):
            #erase character
            del inputStr[i]
            i-=1
        i+=1
    return("".join(inputStr))
    
#ask user text input
para = input("Please enter a paragraph of text:\n")
#call removeNonAlpha function
para = []
removeNonAlpha(para)
#split paragraph by each words and store them in a list
wordList = para.split()
dict1 ={}
#add word to dictionary and count frequency 
for word in wordList:
    if word in dict1:
        dict1[word] +=1
    else:
        dict1[word] = 1
print("Word and Frequency List")
#print out word and its frequency
for word in dict1:
    print(word,":",dict1[word],"times")
#finding top 3 values in dictionary
countN = Counter(dict1)
top = countN.most_common(3)
print("\nTop 3 word frequency in Dictionary")
#print top 3 
for word in top:
    print(word[0],":",word[1],"times")
'''Output
Test(1)
Please enter a paragraph of text:
python is an easy language python is easy to learn and easy to code a lot of python modules that are easy to use go python
Word and Frequency List
python : 4 times
is : 2 times
an : 1 times
easy : 4 times
language : 1 times
to : 3 times
learn : 1 times
and : 1 times
code : 1 times
a : 1 times
lot : 1 times
of : 1 times
modules : 1 times
that : 1 times
are : 1 times
use : 1 times
go : 1 times

Top 3 word frequency in Dictionary
python : 4 times
easy : 4 times
to : 3 times
Test(2)
'''



