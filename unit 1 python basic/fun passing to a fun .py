def sqare(a):
    return a ** 2

def cube(b):
    return b **3

def funTofun(fun,n):
    return fun(n)

a = funTofun(cube,3)

print ('Calling cube function',a)

