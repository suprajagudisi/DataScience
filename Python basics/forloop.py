avail= 10
x= int(input("how many candies"))
i=1
while i<=x:
    if avail<i:
        print("out of stock")
        break
    print("candy")
    i=i+1
print("bye")


