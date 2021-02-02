from threading import *
from time import sleep
class hi(Thread):
    def run(self):
        for i in range(5):

            print("hi")
            # to give little gap between two symulteaneous ececution
            sleep(1)

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

t1= hi()
t2= hello()
t1.start()
# to avoid collision
sleep(0.2)
t2.start()
