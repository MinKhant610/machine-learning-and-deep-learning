class Myclass :
    def __init__ (self,cat1,cat2):
        self.cat1 = cat1 #dot notation
        self.cat2 = cat2
    
    def mInfo(self):
        print ('form mInfo',self.cat1,'',self.cat2)

obj = Myclass ('apple','orange')
print ('obj data :',obj.cat1,'',obj.cat2)
obj.mInfo()
