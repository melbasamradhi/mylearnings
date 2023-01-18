class A:
    def parent(self):
        print("I am the method in parent class")
class B(A):
    def child(self):
        print("I am the method in child class")
class C(B):
    def grandchild(self):
        print("I am the method in grandchild class")

a=A()
a.parent()

b=B()
b.child()
b.parent()

c=C()
c.parent()
c.child()
c.grandchild()

#Hirerical inheritance

class D(A):
    def derived1(self):
        print("I am method in derived class1")

class E(A):
    def derived2(self):
        print("I am method in derived class2")

d=D()
d.derived1()
d.parent()

e=E()
e.derived2()
e.parent()

#multilevel inheritance

class parent1:
    def parentA(self):
        print("I am the method of parent1")

class parent2:
    def parentB(self):
        print("I am the method of parent2")

class child1(parent1,parent2):
    def child1(self):
        print("I am the method of child1")

ch=child1()
ch.child1()
ch.parentA()
ch.parentB()