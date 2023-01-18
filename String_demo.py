#strings are immutable
str1="name"
str2="name"
print(id(str1),id(str2))

str2=str2+" of the programing language"
print(id(str2))

#concatenation and repetation in string
print(str1+"world")

print(str1 *3)

#slicing operator
str="welcome to python learning"
print(str[2:7])
print(str[:11])
print(str[5:])
print(str[1:-9])

#len, in not operators
print(len(str))
print("come" in str)
print("come" not in str)

#iterating string using for loop
for i in str:
    print(i, end=" ") #to print on same line
    #print(str, end=" ")
st=" "
print(st, end="\n")
print(str, end=" foo")