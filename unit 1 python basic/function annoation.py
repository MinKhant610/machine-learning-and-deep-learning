#function annotation formula
#def myfun(a:<expression>,b:<expression>) -> <expression> :
#annotation is => parameter and return of a function
def fun (a:'annotation of a',b:'annotation of b')->'return of function':
    """this is body expression for fun """
    return a*b

print (fun.__annotations__)
print (fun.__doc__)

x = 3
y = 5 
def myfun(a:'some value from funcall')->'multiply'+str(max(x,y))+'time':
    """ doc will return multiply by of max """
    return a*max((x,y))
date = myfun(2)
print (myfun.__doc__)
print (myfun.__annotations__)
