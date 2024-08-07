'''
Created on 2024. 8. 8.

@author: user
'''

try :
    a = int(input('숫자 입력: '))
    b = int(input('숫자 입력: '))
except ValueError as err :
    print('숫자로 입력하세요.')
except :
    print('그 밖의 예외 :' , err)
else :
    print(a + b)
    
print('-----------')

try :
    f = open('a.txt','r')
    str = f.read()
except FileNotFoundError as err:
    print('파일이 없습니다.')
except :
    print('그 밖의 예외 :' , err)
else :
    print(str)    
    
print('-----------')

try :
    a = int(input('숫자 입력: '))
    b = int(input('숫자 입력: '))
    if a<0 or b<0 :
        # 내가 예외 발생
        raise ArithmeticError('음수 입력됨')
except ValueError as err :
    print('숫자로 입력하세요.')
except ArithmeticError as err :
    print('예외 발생:',err)
except :
    print('그 밖의 예외 :' , err)
else :
    print('두 수 모두 양수 입력됨')

    
