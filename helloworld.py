#to print hello world
print("Hello world")

#to add two numbers
x=100
y=300
print(x+y)

""""
to multiply
two numbers
"""
x=2
y=5
print(x*y)

#keywords

import keyword
print(keyword.kwlist)

#various ways to assign value to the variable

a=b=c=10
print(a,b,c)

a,b,c,d,e=10,20.5,"hello",'world',True
print(a,b,c,d)

#to find the data type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#to swap the values
a=10
b=20
b,a=a,b
print(a,b)

#Concatenation

print(10+20)
print(10+10.5)
print(10+True)
print(True+False)
print("welcome"+" to python learning")
print('hello'+' world')
"""
Invalid concatenation
print(10+"welcome")
print(10.5+"welcome")
print(True+"welcome")
"""

x,y=10,20
print("The values of x and y are: ",x,y )

#To take input from the user
a=input("Enter first number")
b=input("Enter second number")
print(a+b)
#concatenation occur because input function takes data as string.

print(int(a)+int(b))

a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a+b)

a=int(input("Enter first number"))
b=float(input("Enter second decimal number"))
print(a+b)

print(int(b))
print(float(a))
