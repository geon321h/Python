'''
Created on 2024. 8. 5.

@author: user
'''

L = [10,30,40]
print('L:',L)

L[1:1] = [20]
print('L : ',L)

L[4:4] = [50]
print('L : ',L)

L.append(60)
print('L : ',L)

L.insert(2, 70)
print('L : ',L)

L2 = []
total = 0
# for i in range(0,5) :
#     num = int(input('숫자를 입력하세요:'))
#     L2.append(num)
#
# for l in L2 :
#     total += l
    
print('L2 : ',L2)
print('total : ',total)

L3 = [30,20,10,70,20]
print(L3.index(20)) # 값의 첫번째 위치
# print(L3.index(80)) # ValueError: 80 is not in list
print(L3.count(20)) # 값의 갯수
L3.remove(20) # 첫번째 값만 삭제
print('L3 : ',L3)

L3.reverse() # 뒤집기
print('L3 : ',L3)

L3.sort() # 정렬 오름차순(기본 false)
print('L3 : ',L3)
L3.sort(reverse = True) # 정렬 내림차순
print('L3 : ',L3)

L4 = ['banana','grape','apple','orange']
print('L4 : ',L4)
L4.sort(reverse = False) # 아스키코드값으로 비교 (첫번째가 같으면 두번째로) 
print('L4 : ',L4)

L5 = ['123','34','56','2345']
print('L5 : ',L5)
L5.sort() # 아스키코드값으로 비교 (첫번째가 같으면 두번째로) 
print('L5 : ',L5)
L5.sort(key=int) # int형으로 생각하여 정렬
print('L5 : ',L5) 



