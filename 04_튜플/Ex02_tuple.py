'''
Created on 2024. 8. 5.

@author: user
'''

t1 = ()
t2 = (1,2,3)
t3 = 1,2,3
t4 = (1,)
t5 = 1,
t6 = (1)
t7 = 1



print(t1,type(t1))
print(t2,type(t2))
print(t3,type(t3))
print(t4,type(t4))
print(t5,type(t5))
print(t6,type(t6))
print(t7,type(t7))

t = (1,2,3)
t2 = t , ('kim','park')
print(t2)
print(t2[1][0])
print(len(t2))

x,y,z = 1,2,3
print(x,y,z)

x,y = y,x
print(x,y)

t=(1,2,3)
x,y,z = t
print(x,y,z)

#t[1] = 22  할수없다

L = list(t)
print(L)
L[1] = 22
print(L)
t = tuple(L)
print(t)


