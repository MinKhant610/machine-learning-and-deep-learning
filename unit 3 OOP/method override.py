class Price():
    def payment(self):
        print ('From Parent class')

class Child(Price):
    def payment (self):
        print ('From Child class')

class GrandChild(Child):
    def payment (self):
        print ('From GrandChild class')

obj = GrandChild()
obj.payment()