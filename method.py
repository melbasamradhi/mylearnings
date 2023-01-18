#calling method m1 from m2 and variable x from m1 to method m2
class myclass:
    def m1(self):
        x=100
        self.x=x
        print("m1 method")
    def m2(self,a):
        print("m2 method",a)
        self.m1()
        print(a+self.x)
c=myclass()
c.m2(10)