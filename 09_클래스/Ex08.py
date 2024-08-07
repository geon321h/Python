'''
Created on 2024. 8. 8.

@author: user
'''

class NumBox :
    def __init__(self,num):
        self.num = num
        self.num2 = num
        
    def __add__(self,num):
        self.num += num
        return '더하기' + str(self.num)
    
    def __radd__(self,num):
        self.num += num
        return '더하기' + str(self.num)
    
    def __sub__(self,num):
        self.num -= num
        return '빼기' + str(self.num)
    
    def __rsub__(self,num):
        self.num -= num
        return '빼기' + str(self.num)
    
print(1+2)
print("1"+"2")
print("1"+str(2))

print('-------')

num = NumBox(40)
print(num.num)
print(num.num2)
print(num.num +50)
print(num + 50)
print(num - 50)
print(50 + num)
print(50 - num)

# 연산자 오버로딩