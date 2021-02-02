def sorted(list):

  for i in range(0,len(list)):
     for j in range(i):
        if list[j]>list[i]:
          list[i],list[j]=list[j],list[i]

  print("sorted",list)
list=[8,9,2]
n=6
sorted(list)
