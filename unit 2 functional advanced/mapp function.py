#map function

#def say():
#   return 'My name is Min Khant'
#fun = print (say)

def fact (x):
    if x < 2:
        return 1
    else:
        return x * fact (x-1)
results = map (fact , range (6) )

for z in results:
    print (z)


