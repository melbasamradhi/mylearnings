def enterage(age):
    if age<=0:
        raise ValueError("only positive numbers are allowed")
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")
try:
    a=int(input("Enter age"))
    enterage(a)
except ValueError:
    print("expection hanled..enter positive values")