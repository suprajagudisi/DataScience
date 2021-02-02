f=open('c:\\data2\\funny.txt',"r")
# f=open('c:\\data2\\funny.txt',"a")
# f.write("\nmy name is")
f1=open("myfile.py","w")
for line in f:
     f1.write(line)
     token=line.split(" ")
     print(len(token))
