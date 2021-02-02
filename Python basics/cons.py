class mathy:
    def __init__(self):
        self.age=30

    def update(self):
        self.age=40
    def compare(self,other):

        if self.age==other.age:
              print("ok")
        else:
              print("not ok")

c1=mathy()
c2=mathy()
c1.update()
c2.age=40
c1.compare(c2)
print(c1.age)
print(c2.age)
