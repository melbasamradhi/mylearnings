a=int(input("Enter the input number"))
b="hello"
print("The given number is: ",a,"and we have to check it is odd or even")
print("Input :%d" %(a))
print("Input :{}".format(a))
print("Input:{0} Name:{1}".format(a,b))
if a%2==0:
    print("Given number ",a," is Even number")
else:
    print("Given number ",a, " is odd number")

#if else in single line
print("Even") if a%2==0 else print("Odd")

#if else in single line but multiple statments
{print("Even"),print("Number")} if a%2==0 else {print("Odd"),print("Number")}
