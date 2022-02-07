from abc import ABC , abstractmethod

class Price(ABC):
    def print_slip(self,amount):
        print ('Pyment amount $ : ', amount)
    @abstractmethod
    def payment (self):
        print ("This is important for abstract method")

class CreditCardPyament(Price):
    def payment(self , amount):
        print ('Payment with CreditCard $ :',amount)

class MobileBanking(Price):
    def payment (self,amount):
        super().payment()
        print ('Payment with Mobile Banking $ :',amount)

obj = CreditCardPyament()
obj.print_slip(1000)
obj.payment(1000)

obj1 = MobileBanking()
obj1.print_slip (2000)
obj1.payment(2000)
