pos=-1
def search(list2,n):
   a=len(list2)

   for i in range(0,a):
      if list2[i]==n:
          globals()['pos']=i
          return True

   return False
list= input("enter the list")
list2=list.split(" ")
list2=[int(e) for e in list2]
n= int(input("enter number"))
if search(list2,n):
    print("found at ",pos)

else:
      print("not found")
