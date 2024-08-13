'''
Created on 2024. 8. 12.

@author: user
'''
import cx_Oracle
con = cx_Oracle.connect('sqlid/sqlpw@localhost:1521/orcl')  

cur = con.cursor()

try:
    dropEmplSeq = 'drop sequence emplseq'
    cur.execute(dropEmplSeq)
except cx_Oracle.DatabaseError:
    print("emplseq 시퀀스 존재하지 않음")

try:
    drop = 'drop table employee'
    cur.execute(drop)
except cx_Oracle.DatabaseError:
    print("employee 테이블 존재하지 않음")

createEmplSeq = 'create sequence emplseq'
cur.execute(createEmplSeq)

createEmployee = '''create table employee (
    num number primary key,
    id varchar2(10),
    part varchar2(10),
    position varchar2(10),
    salary number
)
'''
cur.execute(createEmployee)

selectEmployee = 'select * from employee'
cur.execute(selectEmployee)
print('select 결과')
for row in cur :
    print(row)
print('----------------------')

while True:
    
    while True : 
        id = input('id입력:')
        if len(id) > 10 :
            print('id는 10글자 미만으로 입력하세요')
        else :
            break
    part = input('part입력:')    
    position = input('position입력:') 
    
    while True : 
        try :
            salary = int(input('salary입력:'))
            break
        except ValueError :
            print('salary는 숫자로 입력하세요')
            continue
        
    insert = "insert into employee values(emplseq.nextval,'%s','%s','%s',%d)" % (id,part,position,salary)      
    cur.execute(insert)
    con.commit()    
    retry = input('계속?')
    if retry == 'n' :
        break


selectEmployee = 'select * from employee'
cur.execute(selectEmployee)
print('select 결과')
for row in cur :
    print(row)
print('----------------------')


update_id = input("수정할 id 입력: ")
update_part = input("수정할 part 입력: ")
while True:
    try:
        update_salary = int(input("수정할 급여 입력: "))
        break
    except ValueError:
        print("salary는 숫자로 입력하세요")

updateEmployee = 'update employee set part = :1, salary = :2 where id = :3'
cur.execute(updateEmployee, (update_part, update_salary, update_id))
con.commit()


selectEmployee = 'select * from employee'
cur.execute(selectEmployee)
print('select 결과')
for row in cur :
    print(row)
print('----------------------')

delete_id = input("삭제할 id 입력: ")
deleteEmployee = 'delete from employee where id = :1'
cur.execute(deleteEmployee, (delete_id,))
con.commit()

print("select * from employee 결과")
cur.execute(selectEmployee)
for row in cur:
    print(row)
print('----------------------')

cur.close()
con.close()

