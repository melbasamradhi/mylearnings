x,y=10,20
class demo1:
    c,d=100,200
    def add(self,a,b):
        print("sum of global variables ",x," and ",y,":",x+y)
        print("sum of class variables ",self.c," and ",self.d,":",self.c+self.d)
        print("sum of local variables ",a," and ",b,":",a+b)

    # if global and local variables are having same name
    def sum(self,x,y):
        print("sum of local variables ", x, " and ", y, ":", x + y)
        print("sum of global variables ",globals()['x'], " and ",globals()['y'], ":",globals()['x']+globals()['y'])
d=demo1()
d.add(1000,2000)
d.sum(20,30)

d1=demo1()

#to get the memory location of the object
print(id(d))
print(id(d1))

