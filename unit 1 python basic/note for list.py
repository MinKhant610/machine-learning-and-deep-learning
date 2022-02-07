list = ['apple','orange','grape','pipapple','banana']
list.sort ()
print (list)

list.sort(key=len)
print(list)

list.sort(key=len,reverse=True) 
print(list)

for i in list:
    if i == 'apple' :
        print ('found')
        break
    else:
        print ('not found')

num = [1,2,3,4,5]

for x in num :
    x = x + 3
    print (x)

for y in num [0:3]:
    num.remove(y)
    print ('removing',y)
print (num)

empty = []

for z in range (1,10):
    data = z ** 2
    empty.append (data)
    print ('appending',data)
print (empty)

list = [1,2,3,4]
list1= [1,2,3,4]
print (id(list),id(list1)) #in list they have same value but not in the same memory location

num = (1,2,3,4,5)
#show tuple to list , it really show like list but it cannot work like list
print (num)
print (list(num))