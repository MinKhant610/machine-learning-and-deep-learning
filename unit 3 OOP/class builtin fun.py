#class builtin function
#getattr (obj,name)
#setttr (obj , name , value)
#delattr (obj,name)
#hasattr (obj,name) this function return => Bolean

class Student:
    def __init__ (self , name , id , age ):
        self.name = name
        self.id   = id
        self.age  = age

sobj = Student ('Min Khant' , 9 , 16 )
print (getattr(sobj , 'name'))
print (getattr(sobj , 'age'))

print ('\n__After Using setattr function for age __ \n')

setattr(sobj , 'age' , 23)
print (getattr(sobj , 'age'))
delattr (sobj , 'age')

#to check the age
print (hasattr(sobj , 'age'))

