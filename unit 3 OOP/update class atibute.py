#crud  mean = create read update delete
#crud have two method 1 manually and 2 builtin

class Myclass:
    def __init__ (self):
        self.name = 'Entire'
        self.age  = 16
        self.hooby= 'Coding'

    #For builtin crud

    def update(self):
        self.name = 'Min Khant (MCSC)'
        self.age  = 17
        self.hooby= 'Coding for AI'

o1 = Myclass() #none paremeter

print ('__Before update__')
print (o1.name,'\n',o1.age,'\n',o1.hooby)
print ('')

#This is manually
o1.name = 'Min Khant'
o1.age  = 16
o1.hooby= 'machine learning'

print ('__After Updating Manually')
print (o1.name,'\n',o1.age,'\n',o1.hooby)
print ('')

#For builtin crud
print ('Updating Builtin Crad')
o1.update()
print (o1.name,'\n',o1.age,'\n',o1.hooby)