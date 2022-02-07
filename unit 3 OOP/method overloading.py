class Price:
    def payment(self , x = None , y = None):
        if x!= None and y!=None:
            return x*y
        elif x!= None:
            return x*x
        else:
            return None

obj = Price()
print (obj.payment(10,5))

#this is almost a method overloading and not sure
