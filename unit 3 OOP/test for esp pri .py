class animal:
    def __init__ (self,name,color,age,behaviour):
        self.__name     =name
        self.__color    = color
        self.__age      = age 
        self.__behavior = behaviour

class dog(animal):
    def modify (self,name,color,age,behaviour):
        self.__name     =name
        self.__color    = color
        self.__age      = age 
        self.__behavior = behaviour
    def dget_data(self):
        print (self.__name,self.__color,self.__age,self.__behavior)

obj = dog('Max','black',6,'eat')
obj.modify('super','red',6,'fly')
print (obj.__dict__)
obj.dget_data()
