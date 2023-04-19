#Name: Loc Nguyen
#Lab 9 
'''Objective: 
A student object should contain at least the following fields: name, id, the current quiz score, and the
highest quiz score. A student is allowed to test tests as many times as he/she wishes. Initially the above
two scores are set to 0. Once a student takes a test (should be 5 multiple choice questions), it will
update the current test score (the score for this quiz), may also updates the highest test score if this test
score is higher than the stored highest score. Your should decide whether additional Objects should be
included, e.g. Test objects, Score objects,
'''
import random
class Student:
    def __init__(self, name, id, score, highscore):
        self.name = name
        self.id = id
        self.score = score
        self.highscore = highscore
        pass
#initialize question class with question, choices, and correct answer    
class Question:
    def __init__(self,question:str,choices:dict,correctAnswer:str):
        self.question = question
        self.choices = choices
        self.correctAnswer = correctAnswer
        pass
#create questions
def createQuestion():
    q1 = Question("What was the name of the first human in space?",{"A":"Neil Amstrong","B":"Edwin Aldrin","C":"Yuri Gagarin","D":"Victor Glover"},"C")
    q2 = Question("Personal computers designed specifically around a visual operating system include",{"A":"The TRS-80 Model I","B":"The IBM PC/AT","C":"The Apple Macintosh","D":"All of these"},"C")
    q3 = Question("Mechanism to protect network from outside attack is",{"A":"Formatting","B":"Digital Signature","C":"Firewall","D":"Anti-virus"},"C")
    q4 = Question("Which artist painted Girl with a Pearl Earring?",{"A":"Pablo Picasso","B":"Vincent van Gogh","C":"Johannes Vermeer","D":"Leonardo da Vinci"},"C")
    q5 = Question("What is the role of chlorophyll?",{"A":"To produce energy","B":"To produce sugar","C":"To trap light energy","D":"To trap heat energy"},"C")
    q6 = Question("In which cell organelles does carbon fixation occur?",{"A":"Mitochondria","B":"Golgi Body","C":"Ribosomes","D":"Chloroplasts"},"D")
    q7 = Question("A substance with a pH of 8.4 would be classified as",{"A":"Acidic","B":"Neutral","C":"Safe to consume","D":"Basic"},"D")
    q8 = Question("Which element below is not a transition metal?",{"A":"Zinc","B":"Titanium","C":"Vanadium","D":"Cesium"},"D")
    q9 = Question("Approximately how big is the observable universe?",{"A":"70 billion ly","B":"86 billion ly","C":"63 billion ly","D":"94 billion ly"},"D")
    q10 = Question("Who won the 2022 World Cup hosted by Qatar?",{"A":"France","B":"Brazil","C":"Germany","D":"Argentina"},"D")
    q11 = Question("Approximately how old is the Earth?",{"A":"4.5 billion years","B":"4.2 billion years","C":"3.45 billion years","D":"3.78 billion years"},"A")
    q12 = Question("As of 2023, which country ranks 4th in the world in term of nominal GDP?",{"A":"Germany","B":"Russia","C":"United Kingdom","D":"Japan"},"A")
    q13 = Question("When did California become a US state?",{"A":"1850","B":"1860","C":"1847","D":"1845"},"A")
    q14 = Question("What is the top grossing movie of all time?",{"A":"Avatar","B":"Avengers: Endgame","C":"Titanic","D":"Spider-Man: No Way Home"},"A")
    q15 = Question("As of April 2023, who is the current US Secretary of Education?",{"A":"Miguel Cardona","B":"Betsy DeVos","C":"Anthony Blinken","D":"Janet Yellen"},"A")
    q16 = Question("What is the name of the newest space telescope launched in 2021?",{"A":"Hubble Space Telescope","B":"James Webb Space Telescope","C":"Spitzer Space Telescope","D":"Kepler Space Telescope"},"B")
    q17 = Question("What does the NASDAQ stock exchange stands for?",{"A":"National Association of Sorted Dealers Automated Quotes","B":"National Association of Securities Dealers Automated Quotations","C":"National Association of Securities Defense Automatic Quoting","D":"National Association of Secured Dealers Actuated Quotations"},"B")
    q18 = Question("How many CSU campuses are in the CSU system?",{"A":"19","B":"23","C":"25","D":"21"},"B")
    q19 = Question("How many UC campuses are in the UC system?",{"A":"11","B":"9","C":"10","D":"13"},"B")
    q20 = Question("What is Cal Poly Pomona address?",{"A":"3708 W Temple Ave","B":"3801 W Temple Ave","C":"1403 W Temple Ave","D":"1803 W Temple Ave"},"B")
    
    pass    
#function to select random question
def randomQuestion(questionBank):
    pass

#main function
def main():
    print("Please enter only the letter when selecting answer")
    createQuestion()