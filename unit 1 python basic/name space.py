#global name space
#local name space
#built in name space

a = 2 #this is global name spaces

def outerfun():
    print (a)

    b = 30 # this is local name spaces
    def innerfun():
        print (a)
        a = 30
outerfun()

id (a) #in this statement id is built in name spaces