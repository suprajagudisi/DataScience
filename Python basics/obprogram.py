class myidea:
    def __init__(self,a,b,e,f):
        self.v=a
        self.b=b
        self.e=e
        self.f=f
    def sum(self):
        c= self.v+self.b

        print(c)

    def sub(self):
        su=self.e-self.f
        print(su)


d=myidea(4,5,6,7)
d.sub()
d.sum()

