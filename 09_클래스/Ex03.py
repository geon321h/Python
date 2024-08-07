'''
Created on 2024. 8. 7.

@author: user
'''

class Bank :
    money = 0
    
    def __init__(self,mymoney):
        #print('Bank 생성자')
        rate = 0.3
        self.money = int(mymoney + mymoney * rate)
        
    def show(self):
        print('잔고: ' ,self.money)
        
b1 = Bank(1000)
b2 = Bank(2000)

b1.show()
b2.show()
        
        

    
