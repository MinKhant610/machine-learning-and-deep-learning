#issubclass (child , parent) => return bolean value
#isinstance (obj , class) => return bolean value

class Parent:
    pass

class Child(Parent):
    pass

print (issubclass(Child , Parent))

objOfChild = Child()
print (isinstance (objOfChild , Parent))
print (isinstance (objOfChild , Child))

