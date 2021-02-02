from array import *
x= array('i',[1,2,4,5])

y= int(input("enter the number"))
k=0
for e in x:
    if e==y:

        print(k)
        break
    k+=1
else:
    print("not found")

print("bye")
print(x.index(y))
