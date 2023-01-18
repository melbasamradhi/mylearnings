class demo:
    def inst(self):
        print("This is instance method")

    @staticmethod
    def stat():
        print("This is static method")

    @staticmethod
    def stat1(a):
        print("This is static method with parameter ",a)
d=demo()
d.inst()
demo.stat()
demo.stat1(10)
