'''
Created on 2024. 8. 7.

@author: user
'''

class Person :
    lastname = '김'
    
    def setname(self,name):
        print('self: ' ,self)
        self.fullname = self.lastname + name
        print('self.fullname: ' ,self.fullname)
        
        
p1 = Person()
p2 = Person()

print('p1:',p1)
print('p2:',p2)

print(p1.lastname)
print(p2.lastname)
print(Person.lastname)

p1.setname('연아')
p2.setname('보검')

    
