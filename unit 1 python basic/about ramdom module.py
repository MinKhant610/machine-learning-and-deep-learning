import random 

print (random.random())

#randint()
#randrage()

print ("printing random interger ",random.randint(0,9)) #a <= Number <= b
print ("printing random interger ",random.randrange(0,10,3)) #(starting point,ending point,setp)

#radom.choice
name = ['hello','hi','welcome','halo']
print (random.choice(name))

#radom.unifrom
print (random.uniform(2.5,10.5))

#random.seed()
random.seed(5)
print (random.random())

#random.sample
print (random.sample(name,3)) #to print 3 index value with list

#radom.triangular
print(random.triangular(2.2,10.2))

#random.shuffle
random.shuffle(name)

