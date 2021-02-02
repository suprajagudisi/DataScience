pos=-1
def bsearch(list,n):
  lb= 0
  ub=len(list)-1
  mid=int((ub-lb)/2)
  for e in range(len(list)):
    globals()['pos']=e
    if n <list[mid]:
      ub=mid
      mid=int((ub-lb)/2)
    elif n==list[mid]:
      print("element found at" ,mid)
      break
    else:
      lb=mid
      mid= int((ub-lb)/2)
      mid=lb+mid
def sorted(list):

  for i in range(0,len(list)):
     for j in range(0,6):
        if list[i]<list[j]:
          list[i],list[j]=list[j],list[i]

  print("sorted",list)
list=[2,5,8,9,9,4,6,3,10]
n=6
sorted(list)
print(list)
bsearch(list,n)



