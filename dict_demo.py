friends={'tom':'11','jerry':'22','bob':'33'}
print(friends)

#add
friends['duo']='44'
print(friends)

#retrieve
print(friends['duo'])

#modify
friends['tom']='111'
print(friends)

#delete
del friends['jerry']
print(friends)

for x in friends:
    print(x)
    print(friends[x])
    print(x,":",friends[x])

print(len(friends))

print(friends.get('tom'))
print(friends.keys())