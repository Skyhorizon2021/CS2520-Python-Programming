#Name: Loc Nguyen
#Date: 04/27/2023
'''Objective: 
(5 pts) Write a general sort function that takes a comparison function as well as a list of values
as parameters, then sort the list according to the comparison function provided. May use any
sorting algorithm but do NOT use any predefined sorting function. Test the following:
(1) Sort the integer list [5, 2, 12, 4, 9, 13, 22, 1, 6, 17] to descending order
(2) Sort the name list ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob",
"Joy"] according to alphabetical order.
(3) Sort the tuple list of (name, count) according to name’s alphabetical order. If same name,
then the one has higher count listed first. [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1),
("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)].
'''


#comparison functions
#descending order algorithm for list
def descend(x,y):
    return x > y

#ascending alpha order algo for list
def ascend(x,y):
    return x < y

#sort ascending alpha with higher count for secondary criteria 
def tupleSort(x,y):
    if x == y:
        return x[1] > y[1]
    return x[0] < y[0]

def generalSorter(data,compFunc):
    for i in range(len(data)):
        for j in range(len(data)):
            if compFunc(data[i],data[j]):
                data[i],data[j] = data[j],data[i]
    return data
  

def main():
    intList = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
    intListSort = generalSorter(intList,descend)
    print(intListSort)
    nameList = ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"] 
    nameListSort = generalSorter(nameList,ascend)
    print(nameListSort)
    tupleList = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]
    tupleListSort = generalSorter(tupleList,tupleSort)
    print(tupleListSort)
    
    pass

main()
