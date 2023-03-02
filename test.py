import sys

def encrypt(msg):
    evenList = []
    oddList = []
    for charIndex in range(0,len(msg),2):
        evenList.append(msg[charIndex])
    for charIndex in range(1,len(msg),2):
        oddList.append(msg[charIndex])
    cipherList= oddList + evenList
    for index in range(len(cipherList)):
        sys.stdout.write(cipherList[index])
    return cipherList
def decrypt(msg):
    
#print(len("Hello world!"))
encrypt("Hello,world!")