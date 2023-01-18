from abc import ABC,abstractmethod

class vehicle():
    def __init__(self,a):
        self.a=a

    @abstractmethod
    def set_mileage(self):
        pass
class toyoto(vehicle):
    def set_mileage(self):
        print("mileage value is ",self.a,"kmph")
class maruti(vehicle):
    def set_mileage(self):
        print("mileage value is ",self.a,"kmph")
class mahindra(vehicle):
    def set_mileage(self):
        print("mileage value is ",self.a,"kmph")

t=toyoto(100)
t.set_mileage()

mu=maruti(80)
mu.set_mileage()

mh=mahindra(120)
mh.set_mileage()