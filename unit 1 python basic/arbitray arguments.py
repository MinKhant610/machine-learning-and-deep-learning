def myfun(*args):
    print (args)

myfun(1,2,3,4)

def fun(a,b,*arg):
    print (a)
    print (b)
    print(arg)

fun (1,2,3,4)

def avg (*all):
    length = len (all)
    total  = sum (all)
    
#the following is to fix division zero error
    if length == 0 :
        return 0
    else :
        return total / length
    return total/length
    
result=avg (1,2,3,4,5)
print (result)
