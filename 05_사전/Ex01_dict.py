'''
Created on 2024. 8. 5.

@author: user
'''

d = {'one':'hana','two':'dul','three':'set'}
print(d)
print(type(d))
print(d['two'])

d['four'] = 'net'
print('d:',d)

d['one'] = 1
print('d:',d)
print(len(d))
print(d['three'])
print(len(d['three']))

print('one' in d)
print('dul' in d)
print(d.keys())
print(d.values())
print('one' in d.keys())
print('one' in d.values())

print(d.items())

print()

w1 = "Hello"
w2 = "World~"

print('d:',d)

d = {}
d[w1] = len(w1);
d[w2] = len(w2);
print('d:',d)

d = dict()
print('d:',d)

d = dict(one=1,two=2)
print('d:',d)

d = dict((('one',1),('two',2)))
print('d:',d)

d = dict()
while True :    
    name = input('이름을 입력 : ')
    if (name == '') :
        break;
    score = input('점수를 입력 : ')
    d[name] = score

for i in d :
    print('이름: ',i ,'점수: ',d[i])
    
for i,j in d.items() :
    print(i , j)
    






