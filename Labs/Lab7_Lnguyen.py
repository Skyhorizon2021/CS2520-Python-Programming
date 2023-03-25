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


