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
'''def removeNonAlpha(inputStr):
    i = 0
    while i < len(inputStr):
        #Find characters that doesn't fall within ASCII alphabetic range
        if(ord(inputStr[i])<ord('A') or ord(inputStr[i])>ord('Z') and ord(inputStr[i])<ord('a') or ord(inputStr[i])>ord('z')):
            #erase character
             inputStr[i]
            i-=1
        i+=1
    return("".join(inputStr))'''
 
#ask user text input
para = input("Please enter a paragraph of text:\n")
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
Please enter a paragraph of text:
The moment people are born into this world the moment they receive life their potential is set in stone The fruits of chance Then it will sometimes manifest in various fields That’s the contrivance of the human world They can’t do more than what is carved into their DNA They awaken by the blood passed on from ancestors or by a sudden mutation In other words if you want to create a genius you have to do it from the DNA stage The ones born as an ordinary person will never escape the realms of an ordinary person No matter how blessed their environment is if the student isn’t excellent from the start of they won’t become a genius That 
has been my belief since I was young That was the conclusion from seeing my fellow classmates being given top quality education since infancy That’s why this experiment ran counters to my own way of thinking That being said It isn’t that straightforward that DNA alone could solve it either
Word and Frequency List
The : 3 times
moment : 2 times
people : 1 times
are : 1 times
born : 2 times
into : 2 times
this : 2 times
world : 1 times
the : 9 times
they : 2 times
receive : 1 times
life : 1 times
their : 3 times
potential : 1 times
is : 2 times
set : 1 times
in : 2 times
stone : 1 times
fruits : 1 times
of : 4 times
chance : 1 times
Then : 1 times
it : 3 times
will : 2 times
sometimes : 1 times
manifest : 1 times
various : 1 times
fields : 1 times
That’s : 2 times
contrivance : 1 times
human : 1 times
world : 1 times
They : 2 times
can’t : 1 times
do : 2 times
more : 1 times
than : 1 times
what : 1 times
carved : 1 times
DNA : 1 times
awaken : 1 times
by : 2 times
blood : 1 times
passed : 1 times
on : 1 times
from : 4 times
ancestors : 1 times
or : 1 times
a : 3 times
sudden : 1 times
mutation : 1 times
In : 1 times
other : 1 times
words : 1 times
if : 2 times
you : 2 times
want : 1 times
to : 3 times
create : 1 times
genius : 1 times
have : 1 times
DNA : 2 times
stage : 1 times
ones : 1 times
as : 1 times
an : 2 times
ordinary : 2 times
person : 1 times
never : 1 times
escape : 1 times
realms : 1 times
person : 1 times
No : 1 times
matter : 1 times
how : 1 times
blessed : 1 times
environment : 1 times
is : 1 times
student : 1 times
isn't : 2 times
excellent : 1 times
start : 1 times
of : 1 times
won’t : 1 times
become : 1 times
genius : 1 times
That : 3 times
has : 1 times
been : 1 times
my : 3 times
belief : 1 times
since : 2 times
I : 1 times
was : 2 times
young : 1 times
conclusion : 1 times
seeing : 1 times
fellow : 1 times
classmates : 1 times
being : 2 times
given : 1 times
top : 1 times
quality : 1 times
education : 1 times
infancy : 1 times
why : 1 times
experiment : 1 times
ran : 1 times
counters : 1 times
own : 1 times
way : 1 times
thinking : 1 times
said : 1 times
It : 1 times
that : 2 times
straightforward : 1 times
alone : 1 times
could : 1 times
solve : 1 times
either : 1 times

Top 3 word frequency in Dictionary
the : 9 times
of : 4 times
from : 4 times

Test(3)
Please enter a paragraph of text:
I love going to the movie theater when it is empty and devoid of human life As such it is not difficulty to find a place among the 
best place on the top of the world believe me when I say that books will penetrate the rest of life whether you like it or not bestMarvel movies are blank i should leave and go to the house
Word and Frequency List
I : 2 times
love : 1 times
going : 1 times        
to : 3 times
the : 6 times
movie : 1 times
theater : 1 times
when : 2 times
it : 3 times
is : 2 times
empty : 1 times
and : 2 times
devoid : 1 times
of : 3 times
human : 1 times
life : 2 times
As : 1 times
such : 1 times
not : 2 times
difficulty : 1 times
find : 1 times
a : 1 times
place : 2 times
among : 1 times
best : 1 times
on : 1 times
top : 1 times
world : 1 times
believe : 1 times
me : 1 times
say : 1 times
that : 1 times
books : 1 times
will : 1 times
penetrate : 1 times
rest : 1 times
whether : 1 times
you : 1 times
like : 1 times
or : 1 times
bestMarvel : 1 times
movies : 1 times
are : 1 times
blank : 1 times
i : 1 times
should : 1 times
leave : 1 times
go : 1 times
house : 1 times

Top 3 word frequency in Dictionary
the : 6 times
to : 3 times
it : 3 times
'''

import random
#Task 2
'''Objective: Let L1 be a list of first 100 randomly generated integer numbers in the range [1,
100], let L2 be the integers within the range [1, 100] that are divisible by either 3 or 4.
(1) Use list comprehension to generate L1, L2
(2) Form a set S1 and a frozen set S2 from L1 and L2 respectively.
(3) Create a new set R1 to contain those elements are either in S1 or in S2. Print out how many
elements in R1.
(4) Create a new set R2 to contain those elements are in both S1 and in S2. Print out how many
elements in R2.
(5) Create a new set R3 to contain those elements are in S1 but not in S2. Print out how many
elements in R3'''

L1 = [random.randint(1,100) for i in range(100)]
print("L1:",L1)
L2 = [x for x in range(1,100) if (x%3==0 or x%4==0)]
S1 = set(L1)
S2 = frozenset(L2)
print("S1:",S1)
print("S2:",S2)
#XOR of S1 and S2 
R1 = S1^S2
print("R1:",R1)
print("There are %d elements in R1" % len(R1))
#Intersection of S1 and S2
R2 = S1 & S2
print("R2:",R2)
print("There are %d elements in R2" % len(R2))
#Difference of S1 versus S2 (S1 - S2)
R3 = S1 - S2
print("R3:",R3)
print("There are %d elements in R3" % len(R3))
'''Output
Test(1)
S1: {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 25, 26, 28, 29, 30, 32, 36, 37, 39, 40, 43, 44, 46, 50, 52, 56, 58, 59, 60, 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 85, 86, 87, 89, 94, 96, 97, 98, 99}
S2: frozenset({3, 4, 6, 8, 9, 12, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 33, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60, 63, 64, 66, 68, 69, 72, 75, 76, 78, 80, 81, 84, 87, 88, 90, 92, 93, 96, 99})
R1: {1, 2, 5, 7, 11, 13, 17, 18, 19, 22, 24, 25, 26, 27, 29, 33, 37, 42, 43, 45, 46, 48, 50, 51, 54, 57, 58, 59, 61, 63, 64, 65, 67, 70, 71, 73, 74, 77, 79, 80, 81, 84, 85, 86, 88, 89, 90, 92, 93, 94, 97, 98}
There are 52 elements in R1
R2: {3, 4, 6, 8, 9, 12, 15, 16, 20, 21, 28, 30, 32, 36, 39, 40, 44, 52, 56, 60, 66, 68, 69, 72, 75, 76, 78, 87, 96, 99}
There are 30 elements in R2
R3: {1, 2, 5, 7, 11, 13, 17, 19, 22, 25, 26, 29, 37, 43, 46, 50, 58, 59, 61, 65, 67, 70, 71, 73, 74, 77, 79, 85, 86, 89, 94, 97, 98}
There are 33 elements in R3
Test(2)
S1: {3, 4, 6, 7, 12, 13, 15, 18, 19, 20, 22, 23, 24, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 43, 45, 46, 47, 48, 50, 52, 53, 54, 57, 58, 59, 60, 64, 65, 66, 69, 70, 71, 72, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 87, 88, 90, 91, 92, 93}
S2: frozenset({3, 4, 6, 8, 9, 12, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 33, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60, 63, 64, 66, 68, 69, 72, 75, 76, 78, 80, 81, 84, 87, 88, 90, 92, 93, 96, 99})
R1: {7, 8, 9, 13, 16, 19, 21, 22, 23, 31, 34, 35, 36, 37, 38, 41, 42, 43, 44, 46, 47, 50, 51, 53, 56, 58, 59, 63, 65, 68, 70, 71, 74, 77, 78, 82, 83, 85, 91, 96, 99}
There are 41 elements in R1
R2: {3, 4, 6, 12, 15, 18, 20, 24, 27, 28, 30, 32, 33, 39, 40, 45, 48, 52, 54, 57, 60, 64, 66, 69, 72, 75, 76, 80, 81, 84, 87, 88, 90, 92, 93}
There are 35 elements in R2
R3: {7, 13, 19, 22, 23, 31, 34, 35, 37, 38, 41, 43, 46, 47, 50, 53, 58, 59, 65, 70, 71, 74, 77, 82, 83, 85, 91}
There are 27 elements in R3
Test(3)
S1: {3, 5, 6, 7, 8, 9, 11, 15, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29, 30, 31, 37, 38, 39, 40, 42, 43, 47, 48, 50, 51, 52, 53, 54, 
55, 56, 61, 65, 67, 68, 70, 71, 72, 73, 75, 77, 80, 81, 82, 83, 84, 85, 86, 87, 90, 93, 94, 97, 98}
S2: frozenset({3, 4, 6, 8, 9, 12, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 33, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60, 63, 64, 66, 68, 69, 72, 75, 76, 78, 80, 81, 84, 87, 88, 90, 92, 93, 96, 99})
R1: {4, 5, 7, 11, 12, 16, 19, 21, 22, 23, 25, 29, 31, 32, 33, 36, 37, 38, 43, 44, 45, 47, 50, 53, 55, 57, 60, 61, 63, 64, 65, 66, 67, 69, 70, 71, 73, 76, 77, 78, 82, 83, 85, 86, 88, 92, 94, 96, 97, 98, 99}
There are 51 elements in R1
R2: {3, 6, 8, 9, 15, 18, 20, 24, 27, 28, 30, 39, 40, 42, 48, 51, 52, 54, 56, 68, 72, 75, 80, 81, 84, 87, 90, 93}
There are 28 elements in R2
R3: {5, 7, 11, 19, 22, 23, 25, 29, 31, 37, 38, 43, 47, 50, 53, 55, 61, 65, 67, 70, 71, 73, 77, 82, 83, 85, 86, 94, 97, 98}
There are 30 elements in R3'''

