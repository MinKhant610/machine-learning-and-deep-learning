class Price:
    def payment(self , *args):
        data = 0
        count= 0
        for i in args:
            count +=1
            data = data + i 
        print (f'There are {count} parameter passed')
        return data

obj = Price()
print (obj.payment(10,5))
print (obj.payment(10,5,20))
print (obj.payment(10,20,30,40,50))
print (obj.payment('Aung Aung'))