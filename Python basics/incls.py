class student2:
    def __init__(self,name, rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop('hp',2)

    def show(self):
        print(self.name,self.rollno)


    class laptop:
        def __init__(self,brand,ram):
            self.brand=brand
            self.ram=ram
        def show(self):
              s1.show()
              print(self.brand,self.ram)


s1=student2('ramu',43)
s1.lap.show()


s1.show()
