import sqlite3 as s

con = s.connect('c:\\dd\\adb')
c = con.cursor()

# VSC로 작성해서 RUN하면 SQLLITE에 테이블 생성
# SQLLITE에서 확인 방법은 select * from lunch;

c.execute('drop table if exists lunch')
c.execute('create table lunch(menu, price)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 5000)')
c.execute('insert into lunch values("돈가스", 5000)')

# 삭제하는 방법

c.execute('delete from lunch where menu ="돈가스"')
c.execute('delete from score where name ="한석봉"')

# 국어점수 90점인 사람 지우는 방법

c.execute('delete from score where kor ="90"')

# 읽어와서 파이썬에 뿌리는 방법

c.execute('select * from lunch;')
res = c.fetchall()

print(' 메뉴    가격 ')
print('**************')
for i in res:
    print(i[0],i[1])
print('**************')




con.commit()
c.close()
con.close()
