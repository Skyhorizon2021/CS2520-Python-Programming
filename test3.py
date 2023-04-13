import random

#part c
def aveScore(list):
    sum = 0
    for item in list:
        sum += item[1]
    avgScore = sum/len(list)
    return avgScore

#part d
def sortLst(list):
    ascSort=sorted(list,key = lambda x: (x[0],-x[1],x[2]))
    return ascSort

def main():
    #initialize list
    nameLst = ['Kevin', 'Ada', 'Jenny', 'Ada', 'Betty', 'Sam', 'Kevin', 'Betty', 'Ada', 'Terry', 'Nathan', 'Jenny']
    scores = [80, 75, 68, 95, 85, 76, 78, 88, 92, 84, 82, 86]

    #part a
    ageLst = [random.randint(18,25) for x in range(len(nameLst))]
    list1 = list(zip(nameLst,ageLst))
    print("Part A :",list1)
    #part b
    profile = list(zip(nameLst,ageLst,scores))
    print("Part B:",profile)
    #run part c
    print("Average score:",aveScore(profile))
    #run part d
    print("Part D:",sortLst(profile))
main()
'''Output
Part A : [('Kevin', 25), ('Ada', 21), ('Jenny', 23), ('Ada', 23), ('Betty', 22), ('Sam', 24), ('Kevin', 23), ('Betty', 21), ('Ada', 23), ('Terry', 23), ('Nathan', 19), ('Jenny', 18)]
Part B: [('Kevin', 25, 80), ('Ada', 21, 75), ('Jenny', 23, 68), ('Ada', 23, 95), ('Betty', 22, 85), ('Sam', 24, 76), ('Kevin', 23, 78), ('Betty', 21, 88), ('Ada', 23, 92), ('Terry', 23, 84), ('Nathan', 19, 82), ('Jenny', 18, 86)]
Average score: 22.083333333333332
Part D: [('Ada', 23, 92), ('Ada', 23, 95), ('Ada', 21, 75), ('Betty', 22, 85), ('Betty', 21, 88), ('Jenny', 23, 68), ('Jenny', 18, 86), ('Kevin', 25, 80), ('Kevin', 23, 78), ('Nathan', 19, 82), ('Sam', 24, 76), ('Terry', 23, 84)]'''