from numpy import *
a= array([1,1,2,9,4,5,5,8,9])

print(a.size)
k=0
j=1
index= array([],int)
for i in a:
     if j >=a.size:
            break
     if a[k]==a[j]:
         index=append(index,[k])
         print(index)

     k+=1
     j+=1
d= delete(a,index)
print(d)

