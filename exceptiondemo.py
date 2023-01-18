print("program started")
a=int(input("Enter the dividend"))
b=int(input("Enter the divisor"))
try:
    print(a / b)
except ZeroDivisionError:
    print("division by zero exception handled")
except TypeError:
    print("Type error exception handled")
else:
    print("in else block..no exception")
finally:
    print("in finally block..")





