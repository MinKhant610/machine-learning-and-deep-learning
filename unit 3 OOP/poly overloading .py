class People : #id , age 
    def __init__ (self , id , age ):
        self.id  = id 
        self.age = age
    
    def __add__(self , self1):
        data_id = self.id + self1.id 
        data_age= self.age + self1.age 
        
        return data_id , data_age

p1 = People(123 , 20)
for_self1 = People(101 , 50)
p3 = People (102, 80)

total = p1 + for_self1 
did , dage  = total 
forp3 = People (did , dage)
final_total = forp3 + p3
did , dage = final_total
result = did + dage
print (result)