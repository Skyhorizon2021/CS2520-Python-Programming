#Name: Loc Nguyen
#Project 2 Task 2
'''Objective: Use Python Generator feature to produce a sequence of prime numbers – the generator is able to keep 
generating prime numbers, i.e. no limit. Then, write a main function to do the following: 
(1) generate 50 prime numbers and print out the results (i.e. print out the first 50 prime numbers) 
(2) After the first 50 prime number generated, skip 50 prime numbers, then continue to generate additional 1000 
prime numbers  (i.e. 101st to 1100th). No need to print out all prime numbers, but do print out:  the first one (i.e. 
101st  prime number), the last one (i.e. 1100th prime number), and how much time (in seconds) it takes to perform 
step (2). 
Note: using a normal function to generate prime numbers is NOT acceptable. Must define a generator. '''
import time
#Biggest possible factor is half the number, start with that number
#Then, decrease by 1 until count is 1
start = time.time()
def isPrime(num):
    count = num//2
    while count > 1:
        if num%count==0:
            break
        count-=1
    else:
        return num

def primeGenerator():
    #start with 1st prime number
    n = 2
    #if prime, execution temporarily halt until called
    #if called again, increment by 1 to check and find the next prime num
    #tempt. halt again 
    while True:
        if isPrime(n):
            yield(n)
        n+=1
#print first 50 prime numbers, skip 50, print 101st prime num
#skip, print 1100th prime num
def main():
    gen = primeGenerator()
    print("The first 50 prime numbers are")
    for i in range(1101):
        if i<50:
            print(next(gen))
        elif 51<i<=100:
            next(gen)
        elif i==101:
            print("The 101st prime number is",next(gen))
        elif 101<i<1100:
            next(gen)
        elif i==1100:
            print("The 1100th prime number is",next(gen))
main()
end = time.time()
#output execution time
print("The time of execution is",(end-start),"seconds")
'''Output
The first 50 prime numbers are
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
179
181
191
193
197
199
211
223
227
229
The 101st prime number is 547
The 1100th prime number is 8831
The time of execution is 0.729851484298706 seconds'''