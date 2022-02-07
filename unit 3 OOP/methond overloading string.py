class Price:
    def payment(self ,dataType, *args):
        if dataType == 'int':
            data = 0
            count= 0
            for i in args:
                count +=1
                data = data + i 
            print ('Parameter type is interger')
            print (f'There are {count} parameter passed')
            return data
        elif dataType == "str":
            data = ''
            count= 0
            for i in args:
                count +=1
                data = data + i 
            print ('Parameter type is string')
            print (f'There are {count} parameter passed')
            return data

obj = Price()
print (obj.payment('int',10,5))
print (obj.payment('int',10,5,20))
print (obj.payment('int',10,20,30,40,50))
print (obj.payment('str','Aung ','Aung'))