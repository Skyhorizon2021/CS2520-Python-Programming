#Name: Loc Nguyen
#Date: 04/15/2023
'''Objective:Two articles are stored in two text files, Python.txt and MachineLearning.txt respectively. The following features should be implemented:
1.	Read in the two text files one by one. Prompt the user for the file name, then open the file. If file not found, raise an appropriate exception (not the catch-all exception) and ask user to re-enter.
2.	For each text file, read in line by line, split each line into a list. Remove all non-words or punctuations (assume proper words only contain letters) and convert all uppercases to lowercases. Combine all lines/lists into one big list (one list for each file.) Then, display how many lines total and how many words total in each file. 
3.	Create a set of words (distinct words) from each list, i.e. one set for each file.
4.	Use set operations (one set operation for each subtask) to calculate: (1) total words used in two articles (don’t double count); (2) words appear in article 1 but not in article 2; (3) Words appear in article 2 but not in article 1; (4) words appear in both articles; (5) words not repeated in both articles, i.e. words appearing in one of the articles only. For each subtask, display how many words in each case (i.e. how many elements in each result set), as well as the set content. For example, for question (1), you answer should be in the form of: 105 distinct words used in two articles, and they are: python, machine, learning, …
5.	Count word frequency – form a dictionary with words as key and counts (the appearance in both files) as values, display the words and counts with the most frequent words first, e.g. (‘python’, 5), (‘machine’, 4), (‘learning’, 4), … If two words of same count, doesn’t matter which word appears first. Note: if ‘python’ appears in article 1 three times and in article 2 two times, the count for ‘python’ is 5.
6.	(Bonus, 5 pts) Draw a word cloud (see sample below) based on the word count frequency. '''



def getFilename():
    while True:
        fileName = input("Please enter file name: ")
        try:
            with open(fileName,"r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print("File not found. Try again!")
        except OSError:
            print("Error accessing file. Check file name and path and try again!")
            
getFilename()
        

