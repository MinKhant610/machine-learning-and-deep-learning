class Parent:
    def __init__(self,age): #base class
        self._age = age  #don't touch from outside

class Sub(Parent):
    def getdata (self):
        print (self._age)

obj = Sub(100)
obj.getdata()
