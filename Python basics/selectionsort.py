
def selectionsort(list):
    for i in range(0,len(list)):
        p=i
        for j in range(i,(len(list))):
            if list[p]>list[j]:
                 p=j
        t=list[i]
        list[i]=list[p]
        list[p]=t
list=[8,9,2,4,7]
selectionsort(list)
print(list)
