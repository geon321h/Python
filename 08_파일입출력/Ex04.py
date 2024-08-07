'''
Created on 2024. 8. 7.

@author: user
'''

fr = open('sungjuk.txt','r', encoding='UTF-8')
fw = open('sungjuk_result.txt','w', encoding='UTF-8')

s = fr.readline()
fw.write(s)
fw.seek(fw.tell() - 2) # 개행전 위치로 이동
fw.write('\t합계\n')
for line in fr.readlines() :
    print(line)
    fw.write(line)
    s = line.split()
    
    total = 0
    for i in range(1,len(s)) :
        total += int(s[i])
    
    fw.seek(fw.tell() - 2) # 개행전 위치로 이동
    fw.write(' \t'+str(total)+'\n')
    
fr.close()
fw.close()