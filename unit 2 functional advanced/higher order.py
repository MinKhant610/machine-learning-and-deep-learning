def myfun(fun,*arg,**key):
    return fun (*arg,**key)
testfun = myfun (lambda x,y :x + y,5,10)
print (testfun)

