'''
Created on 2024. 8. 2.

@author: user
'''

#range(시작,끝,증가값) : 시작~끝-1
#range(시작,끝) : 시작~끝-1
#range(끝) : 0~끝-1

for i in range(1,6) :
    for j in range(7,9) :
        print(i,j)
    print('---')
print('####')


for i in range(1,10) :
    print('**',str(i)+'단 **')
    for j in range(2,10) :
        print(i,'*',j,'=',(i*j))
    print('------------')


for i in range(1,6,1) :
    if ( i == 2) :
        continue
    elif (i  == 4) :
        break
    else :
        print(i,end='  ')
print()    