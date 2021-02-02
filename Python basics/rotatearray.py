from array import *

x=array("i",[1,2,3,4,5,6,7])
k=len(x)

d= array(x.typecode,(a for a in x))
k1=len(d)
j=0




for p in range(0,2):

        d[p]=x[k-1]

        for i in range(k-1):
             if j>=7:
              break
             d[j]= x[i]
             j+=1
        print(d)
        j=2
        d[p]=x[k1-2]
print(d)
