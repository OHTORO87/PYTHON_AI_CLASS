#mysql과 연동
import pymysql as my

con = my.connect(host ='127.0.0.1', user='root', password='1234', db='bdb')
c = con.cursor()

c.execute('drop table if exists lunch')
c.execute('create table lunch(menu char(20), price int)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 5000)')
c.execute('insert into lunch values("돈가스", 5000)')

# 읽어와서 파이썬에 뿌리는 방법

c.execute('select * from lunch;')
res = c.fetchall()

'''
print(res[0])
print(res[0][0], res[0][1])
print(res[1][0], res[1][1])
print(res[2][0], res[2][1])
'''



print(' 메뉴    가격 ')
print('**************')
for i in res:
    print(i[0],i[1])
print('**************')

con.commit()
c.close()
con.close()
