
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
            newfile = open(file,"r")
            #read file
            fileData = newfile.read()  
            #normalizing the string according to unicode to remove \xa0 from string
            fileData = unicodedata.normalize("NFKD", fileData)
            #remove Â from file data
            fileData = fileData.replace(u"Â", "")
            #lowercase all letters
            fileData = fileData.lower()
            #remove non-words
            #fileData=re.sub(r'[\w\s]\n','',fileData)
            for char in fileData:
                if ((ord(char)>=97 and ord(char)<=122) or ord(char)==10 or ord(char)==32):
                    pass
                else:
                    fileData = fileData.replace(char,'')
            #count words 
            wordCount = len(fileData)
            #split each lines
            fileLine = fileData.splitlines()
            print(fileLine)
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
    for line in textList:
        
    pass
def main():
    #get the first file
    list1 = getFile()
    #get the second file
    list2 = getFile()
main()