# split() to enter the list by space convert into list
# if you declare cand d inside the function then use return keyword to return the values outside or if you declare the c and variables outside the scope then return is not needed
# if c and is local variable in use the statement to call the function c,d=lis(e)
# and in function return c and d variables
x=input('enter the list')
user=x.split()
print(user)

d=[]
c=[]
 # to convert string list to integer
e=[int(i) for i in user]
def lis(e):


    for i in e:
         pass
         if i %2==0:
             c.append(i)
         else:

             d.append(i)


print(e)
lis(e)
print(sum(c))
print(sum(d))
