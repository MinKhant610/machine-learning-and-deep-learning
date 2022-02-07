class Paraent:
    def paraent (self):
        print ('This is from paraent')

class Aunty(Paraent): # <= this is multilevel inhertiance
    def aunty (self):
        print ('This is from aunty')

class Child (Aunty): # <=
    def child(self):
        print ('This is from child')

obj = Child()
obj.paraent()
obj.aunty()
obj.child()
