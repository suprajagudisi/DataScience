from array import *
a= array("i",[7,1,5,3,6,4])
k=1
j=2
c=[]
for i in a:
    x=len(a)-a[k]
    if x==2:
        break
    b= a[k]
    sell =a[j]
    profit=a[j]-a[k]
    c.append(profit)
    k+=2
    j+=2
print(sum(c))
