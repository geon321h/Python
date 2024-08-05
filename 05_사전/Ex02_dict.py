'''
Created on 2024. 8. 5.

@author: user
'''

p1 = {'kim':30,'park':70,'choi':50}
p2 = {'kim':33,'park':80,'choi':20}

print(p1['park'])
print(p1.get('park'))
print(p1.get('jung'))
print('-----------------')

name = input('이름 입력:')
if(p1.get(name)!=None) :
    print(p1.get(name))
else :
    print('찾는 데이터 없음')
    
p1.update(p2)
print(p1)
print(p2)

p1.clear()
print(p1)

del p2['kim']
print(p2)

print(p2)

    






