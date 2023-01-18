#private variables

class A:
    __x=10
    y=20
    def display(self):
        print(self.__x)
a=A()
a.display()

class B(A):
    pass
b=B()
b.display()
print(b.y)
#print(b.__a)...we can't access private varibles

#private methods

class F:
    def __show(self):
        print("private method")
    def disp(self):
        print("public method")
        self.__show()
f=F()
f.disp()


#getter,setter

class settergetter:
    __s=10
    def setter(self,a):
        self.__s=a
    def getter(self):
        print(self.__s)
sg=settergetter()
sg.setter(100)
sg.getter()


