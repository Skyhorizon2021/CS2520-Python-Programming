
'''Assumptions: \xa0 is part of the unicode encoding and must be removed by normalizing.
Â, hyphens, or periods, among others are non-words so must be removed. Words like general-purpose or high-level is a word when the hyphen is removed'''
import unicodedata,re
from typing import List
def getFile():
    #try to open the file, raise filenotfound exception if file can't be found
    while True:
        try:
            file = input("Please enter file name: ")
            #open file
            newfile = open(file,"r",encoding='utf-8-sig')
            #read file
            fileData = newfile.read() 
            #normalizing the string according to unicode to remove \xa0 from string
            #fileData = unicodedata.normalize("NFKD", fileData)
            #remove Â and ï»¿from file data
            #fileData = fileData.replace(u"Â", "")
            #fileData = fileData.replace(u"ï»¿M", "M")
            #print(fileData)
            #lowercase all letters
            fileData = fileData.lower()
            #remove non-words & punctuation
            for char in fileData:
                if ((ord(char)>=97 and ord(char)<=122) or ord(char)==10 or ord(char)==32):
                    pass
                else:
                    fileData = fileData.replace(char,' ')
            #count words 
            wordList = fileData.split()
            wordCount = len(wordList)

            #split each lines
            fileLine = fileData.splitlines()
            #print(fileLine)
            #close file
            newfile.close()
        #execute when error is found
        except FileNotFoundError:
            print("File not found. Try again!")
            continue
        #execute only when no exception happened
        else:
            if len(fileLine) >1 or len(fileLine)==0:
                print("There are",len(fileLine),"lines in",file)
            else:
                print("There is",len(fileLine),"line in",file)
            if wordCount >1 or wordCount==0:
                print("There are",wordCount,"words in",file)
            else:
                print("There is",wordCount,"word in",file)
            return fileLine
#function to create sets
def createSet(textList : List):
    newSet = set()
    #for each line, split it based on space, and add the words to the set 
    for line in textList:
        wordList = line.split()
        #print(wordList)
        #remove empty string element
        #line = [i for i in line if i]
        for word in wordList: 
            newSet.add(word)
        '''#check for multiple words on a line
        if len(line)>1:
            for word in line:
                newSet.add(word)
        #if only 1 word on the line, just add it to the set
        else:
            newSet.add(line)'''
    #print(newSet)
    
    return newSet
def wordFrequency(list1, list2):
    
    pass
def main():
    #get the first file
    list1 = getFile()
    #get the second file
    list2 = getFile()
    #create set of words for first list
    set1 = createSet(list1)
    #create set of words for second list 
    set2 = createSet(list2)
    #to find total words used in two articles is same as union
    totalWord = set1|set2
    print("\n")
    print(len(totalWord),"distinct words used in two articles. They are")
    for word in totalWord:
        print(word,end=', ')
    #words in article 1 but not in article 2
    diff1 = set1-set2
    print("\n")
    print(len(diff1),"words are in article 1 but not in article 2. They are")
    for word in diff1:
        print(word,end=', ')
    #words in article 2 but not in article 1
    diff2 = set2-set1
    print("\n")
    print(len(diff2),"words are in article 2 but not in article 1. They are")
    for word in diff2:
        print(word,end=', ')
    #words in both articles
    intersect = set1&set2
    print("\n")
    print(len(intersect),"words are in both article 1 and article 2. They are")
    for word in intersect:
        print(word,end=', ')
    #XOR or union of differences
    xOR = set1^set2
    print("\n")
    print(len(xOR),"words are not repeated article 1 and article 2. They are")
    for word in xOR:
        print(word,end=', ')
main()