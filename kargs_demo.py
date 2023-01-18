
def show(a,d,c):
    print(a,d,c)

show('sam','pam','ham')

#method1
friends={"a":"11","d":"22","c":"33"}
show(**friends)

#method2

def show1(**kargs):
    for i, j in kargs.items():
        print(i,j)

show1(a="11",b="22",c="33")
show1(a='11',b='22',c='33')





