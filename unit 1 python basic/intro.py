a = complex (1+2)

print(a)
print (a.real)
print (a.imag)

a = 10
b = 20
c = 30

if (a > b) and (a > c) :
    largenumber = a
elif (b > a) and (b > c):
    largenumber = b
else:
    largenumber = c
print ("largenumber is :",largenumber)