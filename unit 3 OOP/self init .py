class Myclass:
    def __init__ (self,xAxis,yAxis):#Special Method
        self.xAxis=xAxis
        self.yAxis=yAxis

obj1  = Myclass(10,20)
obj2 = Myclass(1.1,2.2)
print ('for obj1 ',obj1.xAxis,obj1.yAxis)
print ('for obj2',obj2.xAxis,obj2.yAxis)
