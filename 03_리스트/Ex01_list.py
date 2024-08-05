'''
Created on 2024. 8. 5.

@author: user
'''

L = [1,2,3]
print('L:',L)
a=10
print(type(a))
print(type(L))
print(L[0])
print(L[1])
print(L[2])
print(L[-0])
print(L[-1])
print(L[-2])
print(L[-3])
print('len(L):',len(L))
print(L.__len__())

for i in range(0,L.__len__()) :
    print(L[i])
    
for i in L :
    print(i,end=" ")
print()

print( 3 in L )
print( 7 in L )
print( L + L )
print( L * 3 )

print(L[1])    
print(L[1:2])
print(L[1:3])
print(L[1:50]) # 있는 방까지만 가지고온다 1:3과 같다
print(L[1:]) # 시작위치부터 끝까지 가지고온다
print(L[:2]) # 0번부터 끝위치까지 가지고온다
print(L[:]) # 0번부터 끝까지 가지고온다

L2 = [10,20,30,40,50,60,70,80]
print('L2:',L2)
print(L2[1:3])
print(L2[1::3]) #:만큼 건너뜀
print(L2[0::2])
print(L2[::-2])

L3 = ['apple','banana',100,200]
print('L3:',L3)
print(L3[1])
L3[1:1] = [300]
print('L3:',L3)

L3[1:2] = [1,2,3,4,5]
print('L3:',L3)

L3[2:3] = ['tomato']
print('L3:',L3)

L3[0:2] = []
print('L3:',L3)

L3[4:] = [10]
print('L3:',L3)

del(L3[2])
print('L3:',L3)

del(L3)

