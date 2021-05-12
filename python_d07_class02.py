
### 시간을 알아보자 ###
import time as t
print(t.time())
1620785922.4330592

>>> t1 = t.gmtime()
>>> print('{}/{}/{}'.format(t1.tm_year, t1.tm_mon, t1.tm_mday))
2021/5/12
>>> print('{}/{}/{}'.format(t1.tm_hour, t1.tm_min, t1.tm_sec))
2/26/57
>>> t1 = t.localtime() #내 컴퓨터 시간
>>> print('{}시 /{}분 /{}초'.format(t1.tm_hour, t1.tm_min, t1.tm_sec))
11시 /29분 /7초

### datetime 이용 ###
>>> import datetime as d
>>> d.datetime.now()
datetime.datetime(2021, 5, 12, 11, 31, 42, 61837)
>>> n = d.datetime.now()

>>> print('{}시 /{}분 /{}초'.format(n.hour, n.minute, n.second))
11시 /32분 /15초

### 5월만 출력 ###
>>> print(cal.month(2021,5))


##### 달력 보기 #####

>>> import calendar as cal
>>> 
>>> now = cal.calendar(2021)
>>> print(now)
