list1=list()
list2=list([22,33,44])
list3=list(["mel","sony","sam","puppy"])
list4=list("python")
print(list1)
print(list2)
print(list3)
print(list4)
l=[1,2,3,23,45]
l.reverse()
print(l)
l.sort()
print(l)
l.remove(1)
print(l)
a=[12,13,45,4,3,2]
l.extend(a)
print(l)
l.append(3)
print(l.count(3))
l.pop(3)
print(l)
l.remove(12)
print(l)

for x in range(10):
    print(x, end=" ")
d=" "
print(d, end="\n")
l=[x for x in range(10)]
print(l)

l=[x+1 for x in range(10)]
print(l)

l=[x for x in range(10) if x%2==0]
print(l)