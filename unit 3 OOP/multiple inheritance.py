class Paraent:
    def paraent (self):
        print ('This is from paraent')

class Aunty:
    def aunty (self):
        print ('This is from aunty')

class Uncle:
    def uncle (self):
        print ('This is from uncle')

class Child (Paraent,Aunty,Uncle):
    def child(self):
        print ('This is from child')

obj = Child()
obj.paraent()
obj.aunty()
obj.uncle()
obj.child()

