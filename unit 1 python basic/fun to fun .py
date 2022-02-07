def sqare(a):
    return a**2

def cube(b):
    return b ** 3

def num(number):
    if number == 1 :
        return sqare
    else:
        return cube

sq=num(1)
print (sq(10))

cu = num(2)
print (cu(3))

