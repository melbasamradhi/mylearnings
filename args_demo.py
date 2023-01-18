def addition(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("sum is ",sum)

addition(2,3)
addition(20,30,123,245,60,58)

#passing list as arguments
def display(a,b,c,d,e):
    print(a,b,c,d,e)

l=[1,2,3,4,5]

display(*l)