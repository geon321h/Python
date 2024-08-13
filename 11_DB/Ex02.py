'''
Created on 2024. 8. 9.

@author: user
'''
import cx_Oracle
# 검색 Anaconda Prompt -> conda install cs_Oracle

con = cx_Oracle.connect('sqlid/sqlpw@localhost:1521/orcl')

print(type(con))

cur = con.cursor() # 결과에 접근하는 것 (creat , delete 등의 실행 결과)

try :
    drop = 'drop table sungjuk'
    cur.execute(drop)
except cx_Oracle.DatabaseError :
    print('테이블 존재하지 않음')

try :
    dropseq = 'drop sequence sgseq'
    cur.execute(dropseq)
except cx_Oracle.DatabaseError :
    print('시퀀스 존재하지 않음')

seq = ' create sequence sgseq '
cur.execute(seq)

create =  '''create table sungjuk(
      name VARCHAR2(10),
      kor number,
      eng number
    )
'''
cur.execute(create)

cur.execute('select * from sungjuk')
for row in cur:
    print(row)
print('-'*20)

L = [('손흥민',33,77),('설현',77,88),('나연',33,60),('김연아',80,90)]
cur.executemany('insert into sungjuk values(:1,:2,:3)',L)
cur.execute('select * from sungjuk order by name desc')
for row in cur:
    print(row)
print('-'*20)

print('----------------------------------------')
cur.execute('select * from sungjuk order by name desc')
print(cur.fetchone())
print('-----------')
print(cur.fetchall())
print('-----------')

print('----------------------------------------')

eng_L = (70,89)
cur.execute('select * from sungjuk where eng >= :1 and eng <= :2 order by name desc',eng_L)
print('between: ',cur.fetchall())
cur.execute('select * from sungjuk where eng between :1 and :2 order by name desc',eng_L)
print('부등호: ',cur.fetchall())
cur.execute('select * from sungjuk where eng >= %d  and eng <= %d order by name desc' % (eng_L[0],eng_L[1]))
print('%d: ',cur.fetchall())

update_name = "설현"
update_kor = 100
updateSql = "update sungjuk set kor = :1 where name = :2"
cur.execute(updateSql,(update_kor,update_name))
cur.execute('select * from sungjuk order by name desc')
print(cur.fetchall())

cur.execute("update sungjuk set kor = %d where name = '%s'" % (update_kor,update_name))
cur.execute('select * from sungjuk order by name desc')
print(cur.fetchall())

delete_name = "손흥민"
deleteSql = "delete sungjuk where name = :1"
cur.execute(deleteSql,(delete_name,))
cur.execute('select * from sungjuk order by name desc')
print(cur.fetchall())

cur.execute("delete sungjuk where name = '%s'" % delete_name)
cur.execute('select * from sungjuk order by name desc')
print(cur.fetchall())

con_name = '연'
cur.execute("select * from sungjuk where name like :1 ",(('%'+con_name+'%'),))
print(cur.fetchall())

cur.close()
con.close()




