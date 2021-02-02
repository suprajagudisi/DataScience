

def fat(n):
    a=1
    b=2
    c=0
    for i in range(1,n):

        c=a*b
        a=c
        b+=1
    return c

c=fat(5)
print(c)
# we can just use f=f*i
#for i in range(1,n+1):
 #   f=f*i

