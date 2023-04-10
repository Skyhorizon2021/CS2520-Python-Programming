#write strings one by one, i.e. write(str)
fp=open('data1.txt', 'w')
fp.write("hello\t")
fp.write("how are you")
fp.write("\n")
fp.write("thank you ")
fp.write("bye\n")
fp.close()

#print content
fp=open('data1.txt','r')
content1 = fp.read()
print("data1.txt\n" + content1)
fp.close()

#writelines(): write a sequence, i.e. a list or a tuple into a file
fp=open('data2.txt', 'w')
fp.writelines(["hello\t", "how are you", "\n", "thank you ", "bye\n"])
fp.close()

#print content
fp=open("data2.txt",'r')
content2 = fp.read()
print("data2.txt\n" + content2)
fp.close()

'''Output:
data1.txt
hello   how are you
thank you bye

data2.txt
hello   how are you
thank you bye
Comparison: THey have identical output despite using different methods'''