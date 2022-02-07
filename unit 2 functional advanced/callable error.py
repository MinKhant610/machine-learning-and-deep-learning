class myClass :
    def __init__ (self,x=0):
        print ('from class')
        self.counter = x 
    
    def __call__(self,x=1):
        print ('updating value')
        self.counter += x
    
    def myfun(self,z = 1):
        print ('from myfun new __')
        self.counter +=z

myobj = myClass()
inobj = myClass()
myfunobj = myClass()

print (myClass.__init__(myobj,20))

myobj