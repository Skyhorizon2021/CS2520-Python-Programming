'''Lab 6 Task 3
Objective:
1. Given a tuple of names, say (“Winny”, “Ada”, “Lev”, “Kay”, “Jack”, “Sam”, “Mark”), and a list of ages, 
e.g. [20, 18, 22, 16, 20, 18, 18], use zip feature to form a tuple of tuples, i.e.  ((“Winny”, 20), (“Ada”, 18), 
(“Lev”, 22), (“Kay”, 16), (“Jack”, 20), (“Sam”, 18), (“Mark”, 18))
2. From the tuple of (name, age), find the name who is the youngest as well as the average age.
3. Sort the tuple into the descending order of the scores. If score is same, arrange the tuples in 
alphabetical order of names. E.g. the above should be: ((‘Lev, 22), (‘Jack’, 20), (‘Winny’, 20), ...)'''
#initilize var
sum = 0
count = 0
#sort by 2nd element
def sortTuple(tup):
    ascSort=sorted(tup,key = lambda x: x[1])
    return ascSort
#reverse sort by 2nd element and alphabetically by 1st element 
def reverseSortTuple(tup):
    desSort=sorted(tup,key = lambda x: (-x[1],x[0]))
    return desSort
#initialize tuples and zip them
t1 = ("Winny","Ada","Lev","Kay","Jack","Sam","Mark")
t2 = (20,18,22,16,20,18,18)
t3 = zip(t1,t2)
sort_Tuple = sortTuple(tuple(t3))
minPair = sort_Tuple[0]

#assign age and name value
minName = minPair[0]
minAge = minPair[1]

#sort in descending order
revSort_Tuple = reverseSortTuple(sort_Tuple)
#get sum
for i in sort_Tuple:
    sum += i[1]
    count += 1

#calculate average age
avgAge = sum / count

print("Tuple in descending order",revSort_Tuple)
print("Average age is %.2f" % avgAge)
print("The youngest is",minName,"at",minAge,"years old")

#reinitialize var
sum = 0
count = 0
#second test pair
t4 = ("Psaki","Yuki","Lelouch vi Britannia","Zero","Bald Cape","Hinata","Shinichi","Doyle")
t5 = (15,6,20,20,31,14,7,49)
t6 = zip(t4,t5)
sort_Tuple = sortTuple(tuple(t6))
minPair = sort_Tuple[0]

#assign age and name value
minName = minPair[0]
minAge = minPair[1]

#sort in descending order
revSort_Tuple = reverseSortTuple(sort_Tuple)
#get sum
for i in sort_Tuple:
    sum += i[1]
    count += 1

#calculate average age
avgAge = sum / count

print("Tuple in descending order",revSort_Tuple)
print("Average age is %.2f" % avgAge)
print("The youngest is",minName,"at",minAge,"years old")
'''Output
Test(1)
Tuple in descending order [('Lev', 22), ('Jack', 20), ('Winny', 20), ('Ada', 18), ('Mark', 18), ('Sam', 18), ('Kay', 16)]
Average age is 18.86
The youngest is Kay at 16 years old
Test(2)
Tuple in descending order [('Doyle', 49), ('Bald Cape', 31), ('Lelouch vi Britannia', 20), ('Zero', 20), ('Psaki', 15), ('Hinata', 14), ('Shinichi', 7), ('Yuki', 6)]
Average age is 20.25
The youngest is Yuki at 6 years old'''


