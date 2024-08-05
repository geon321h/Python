'''
Created on 2024. 8. 2.

@author: user
'''

#range(시작,끝,증가값) : 시작~끝-1
#range(시작,끝) : 시작~끝-1
#range(끝) : 0~끝-1

total = 0
for i in range(1,10,3) :
    print(i)
    total += i
print(total)

odd_total = 0
even_total = 0
for i in range(1,11) :
    if i%2 == 0 :
        even_total += i
    else :
        odd_total += i
print("홀수 총합:",odd_total)
print("짝수 총합:",even_total)