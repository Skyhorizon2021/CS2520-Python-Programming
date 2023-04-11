numList = []

fileNotFound=True
while fileNotFound:
    try:
        filename = input("Enter the name of file to open: ")
        file = open(filename,'r')
        print()
        for number in file:
            try:
                num = float(number)
                numList.append(num)
            except ValueError:
                numList.append(0.0)
        print(numList)               
        file.close()
        fileNotFound=False
        
    except FileNotFoundError:
        print("File not found.")
        fileNotFound=True

'''Output:
Enter the name of file to open: elevent.txt
File not found.
Enter the name of file to open: new.txt
File not found.
Enter the name of file to open: output.txt

[102.0, 20.5, 0.0, 0.0, 30.2, 7.0, 0.0, 93.0, 0.2, 3.0, 4.0, 7.0, 0.0, 0.0, 0.0, 78.0, 2312.123, 99.0, 2.0, 0.0]  
'''




