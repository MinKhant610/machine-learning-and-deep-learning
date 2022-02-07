class Main:
    def mymethod(self):#normal method
        self.x=10
        self.y=20

ob1 = Main()
ob2 = Main()
ob1.mymethod()
ob2.mymethod()
print (ob1.x , ob1.y)
print (ob2.x , ob2.y)