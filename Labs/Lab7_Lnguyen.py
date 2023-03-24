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

wordList = []
para = input("Please enter a paragraph of text:\n")
wordList.append(para)