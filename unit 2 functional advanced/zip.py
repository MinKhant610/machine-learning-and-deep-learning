itr1 = [1,2,3,4,5]
itr2 = [10,20,30,40]

result = zip (itr1 , itr2)
print (result)

for i in result :
    print (i)

print ('_____another program \n')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k']

def VowelFilter(alphabet):
    vowel = ['a','e','i','o','u']
    if (alphabet in vowel) :
        return True
    else :
        return False

FilterVowle=filter (VowelFilter , alphabet)

print (FilterVowle)

for x in (FilterVowle):
    print (x)
