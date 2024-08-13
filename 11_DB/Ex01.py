'''
Created on 2024. 8. 9.

@author: user
'''
import cx_Oracle
# 검색 Anaconda Prompt -> conda install cs_Oracle

con = cx_Oracle.connect('sqlid/sqlpw@localhost:1521/orcl')

print(type(con))

cur = con.cursor() # 결과에 접근하는 것 (creat , delete 등의 실행 결과)

drop = 'drop table person'
cur.execute(drop)

dropseq = 'drop sequence perseq'
cur.execute(dropseq)

seq = ' create sequence perseq '
cur.execute(seq)

create =  '''create table person(
      num number PRIMARY KEY,
      id VARCHAR2(10),
      name VARCHAR2(10),
      addr VARCHAR2(10)
    )
'''
cur.execute(create)

cur.execute('select * from person')
for row in cur:
    print(row)
print('-'*20)

insert = "insert into person values(perseq.nextval,'hong','길동','서울')"
cur.execute(insert)

insert = "insert into person values(perseq.nextval,'kim','연아','부산')"
cur.execute(insert)

insert = "insert into person values(perseq.nextval,'park','지성','제주')"
cur.execute(insert)

cur.execute('select * from person')
for row in cur:
    print(row,'/',row[2])
print('-'*20)

cur.execute("update person set name='길순' where id='hong'")
cur.execute('commit')

cur.execute('select * from person')
for row in cur:
    print(row,'/',row[2])
print('-'*20)

cur.execute("delete person where id='hong'")
cur.execute('commit')

cur.execute('select * from person')
for row in cur:
    print(row,'/',row[2])
print('-'*20)

cur.close()
con.close()
