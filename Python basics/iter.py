class topten:
    def __init__(self):
        self.num = 1
    def  __iter__(self):
        return self
    def __next__(self):
        if self.num<=20:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=topten()
print(next(values))
print(next(values))
for i in values:
   print(i)
