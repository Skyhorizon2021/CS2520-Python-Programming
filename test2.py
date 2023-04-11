numList = []

fileNotFound=True
while fileNotFound:
    try:
        filename = input("Enter the name of file to open: ")
        file = open(filename,'r')
        for number in file:
            try:
                number.
                num = float(number)
                numList.append(num)
            except ValueError:
                numList.append(0.0)               
        file.close()
        fileNotFound=False
        
    except FileNotFoundError:
        print("File not found. Please re-enter the file name: ")
        fileNotFound=True

'''
filename = input("Enter the name of file to open: ")
file = open(filename,"r")
content = file.read()
print(content)
file.close()
'''




