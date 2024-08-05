'''
Created on 2024. 8. 5.

@author: user
'''

a = [10,30,40]

for i in range(0,len(a)) :
    print(a[i],end=" ")
print()

for i in range(0,a.__len__()) :
    print(a[i],end=" ")
print()
    
for i in a :
    print(i,end=" ")
print()

L = [['kim','park'],[10,20,30]]
print('L: ',L)
print(L[0])
print(L[1])
print(L[0][0])
# print(L[0][2]) # IndexError: list index out of range
print(L[1][2])

print(len(L)) # 행의 갯수
print(len(L[0])) # 열의 갯수
print(len(L[1])) # 열의 갯수

for i in L :
    for a in i :
        print(a, end=' ')
    print()
print()

L2 = [i*i for i in range(10)]
print('L2: ',L2)

a = [1,2,3]
b = ['x','y']

L3 = [[i,j]
            for i in a
                for j in b    
    ]
print('L3: ',L3)

jumsu = [90,25,40,87,52]
print('합계:',sum(jumsu))
print('최대:',max(jumsu))
print('최소:',min(jumsu))

# 인수 하나 일시 (index,값) 형식
for a,b in enumerate(jumsu) : 
    print(a,'/',b)





    