'''
Created on 2024. 8. 5.

@author: user
'''

L = [1,2,3,4,5]
print('L:',L)
print('L:',type(L))


t = (1,2,3,4,5)
print('t:',t)
print('t:',type(t))

print(t[0]) 
print(t[-1])
print(len(t))
print(t[0:2])
print(t[2:])
print(t[:2])
print(t[::2])

for i in range(0,len(t)) :
    print(t[i],end="\t")
print()

for i in t :
    print(i,end=" ")
print()

print(t*3)
print(3 in t)


