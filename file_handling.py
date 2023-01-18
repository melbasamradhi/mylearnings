f=open('demofile3.txt','w')
f.write("This is my first line\n")
f.write("This is my second line\n")
f.write("This is my third line\n")
f.write("This is my fourth line\n")
f.close()

f=open('demofile3.txt','a')
f.write("This is a newly appended line\n")
f.close()

f=open('demofile3.txt','r')
#print(f.read())
#print(f.read(5))
#print(f.readline())
#print(f.readlines())

for i in f:
    print(i)

f.close()




