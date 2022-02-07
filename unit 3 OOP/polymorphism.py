class AgAg:
    def human (self):
        print ('AgAg is a programmer')
        print ('AgAg is alway coding')

class MgMg:
    def human (self):
        print ('MgMg is a hacker')
        print ('MgMg is alway learning')

class KoKo:
    def human (self):
        print ('KoKo is a scientist')
        print ('KoKo is alway testing')

class People:
    def fun (self , obj):
        obj.human()

agag   = AgAg()
mgmg   = MgMg()
koko   = KoKo()
people = People()

people.fun(agag)

mylist = [agag,mgmg,koko]
for obj in mylist:
    people.fun(obj)

