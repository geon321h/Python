'''
Created on 2024. 8. 8.

@author: user
'''

x=4
y=0
L=[1,2,3]

try :
    print(x/2)
    print(x/y)
    print(L[5])
except ZeroDivisionError as err :
    print('err:',err)
except IndexError as err :
    print('err:',err)
except :
    print('그 밖의 예외 except에서 처리함')
finally:
    print('finally')
print('-----------')
    
