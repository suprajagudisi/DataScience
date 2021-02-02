def topten():
    n=1
    while n<=10:
        sq=n*n;

        n+=1
        yield sq

for i in topten():
    print(i)
