import inspect
from inspect import isfunction,ismethod
import math
def myfun(x,y,z=10,*,kw1,kw2=2):
    return x+y

print (myfun.__name__) #name
print (myfun.__defaults__) #positinal argument
print (myfun.__kwdefaults__) #keyword only arguments
print (myfun.__code__.co_varnames)
print (myfun.__code__.co_argcount)
#to test inspect
print (inspect.getsource(myfun))
print (inspect.getcomments(myfun))
#to test inspect => isfunction and ismethod 
print ('checking is function',isfunction(myfun))
print ('checking is method',ismethod(myfun))
print (inspect.getmodule(print))
print (inspect.getmodule(ismethod))
#to test math
print (inspect.getmodule(math.sin))