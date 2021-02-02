# class variables and instance variables or namespaces
# class method and instance method(accesor andd mutator) and static method
class student:
# class variable
     school="myworld"
     def __init__(self,m1,m2):
         self.m1=m1
         self.m2=m2
     def sum(self):
         return (self.m1+self.m2)
     # accesor or instance method
     def get_marks(self):
          return self.m1

     # mutator or instance method
     def set_marks(self,value):
          self.m1=value
          print(self.m1)
     # class method
     @classmethod
     def info(cls):
          student.school="telusko"
          return student.school
     # static method
     @staticmethod
     def stat_inform():
         print("Iam here")
c1 =student(30,40)
print(c1.sum())
print(c1.get_marks())
c1.set_marks(20)

print(student.info())
student.stat_inform()

