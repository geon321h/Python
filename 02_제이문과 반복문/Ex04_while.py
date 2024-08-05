'''
Created on 2024. 8. 5.

@author: user
'''

i=1
while i<5 :
    print(i)
    i += 1
print('while문 끝')

i=1
while True :
    print(i)
    i += 1
    if(i>5) :
        break
print('while문 끝')

cnt = 0
total = 0
while True :
    num = int(input('숫자를 입력하세요:'))
    cnt += 1
    total += num
    if (num < 0) :
        break
avg = total/cnt
print('반복횟수 :',cnt)
print('합계 :',total)
print('평균 :',avg)
a = avg//10
for i in range(0,int(a)) :
    print('*',end='')
