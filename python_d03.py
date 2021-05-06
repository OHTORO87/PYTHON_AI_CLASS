Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #20210506 python class
>>> # or : |, and : &, ^ : XOR(배타적 OR)카넷?, ~ : 논리 NOT
>>> #이산수학에서 개념 다시 확인해볼것
>>> 
>>> # bit연산/이진연산 개념 확인!
>>> for i in 3,4,5
SyntaxError: invalid syntax
>>> for i in 3,4,5 :
	print(i)

	
3
4
5
>>> #range()를 넣는다면 어디에 넣어야하나?
>>> # 오늘은 list, tuple, set, dict 쓰는 법을 배운다.
>>> ㅁ= [3, 6, 9]
>>> a = [3, 6, 9]
>>> type(a)
<class 'list'>
>>> a[0]
3
>>> a[1]
6
>>> a[2]
9
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> len(a)
3
>>> b = [6, 8, 9]
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]
>>> a + b
[3, 6, 9, 6, 8, 9]
>>> ab = a + b
>>> ab
[3, 6, 9, 6, 8, 9]
>>> #c나 java는 이거 안된다
>>> #졸라 편하고 직관적
>>> a.extend(b)
>>> a
[3, 6, 9, 6, 8, 9]
>>> # extend는 합치는거
>>> len(a)
6
>>> a[5]
9
>>> a[5] = 99 #데이터를 99로 바꿔버리기
>>> ㅁ
[3, 6, 9]
>>> a
[3, 6, 9, 6, 8, 99]
>>> a[6] = 77
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a[6] = 77
IndexError: list assignment index out of range
>>> #a에 6번째 데이터를 넣는건 안되네?
>>> a.append(77)
>>> a.append(44)
>>> a
[3, 6, 9, 6, 8, 99, 77, 44]
>>> #append는 꼬랑지에 데이터 추가!!
>>> a
[3, 6, 9, 6, 8, 99, 77, 44]
>>> a.append([66, 33])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33]]
>>> a.extend([22, 88])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> #append와 extend 차이 생각해보기!
>>> a.insert(2, 80) #2번쨰 자리에 80을 넣어라
>>> ㅁ
[3, 6, 9]
>>> a
[3, 6, 80, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(0, 1004) #맨앞에 1004를 넣으시오
>>> a
[1004, 3, 6, 80, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.pop()
88
>>> a.pop()
22
>>> #맨뒤에 값이 빠져 나온다.
>>> a
[1004, 3, 6, 80, 9, 6, 8, 99, 77, 44, [66, 33]]
>>> #빠져 나온 값은 사라짐?
>>> a.index(3)
1
>>> a.index(99)
7
>>> #몇번쨰에 데이터가 있는지 알려줌.
>>> #pop으로 뺴낸 값은 확인하고 버려버리는것이여
>>> #a안에 [66, 33]값은 집합안의 집합의 개념이다
>>> t = a.pop()
>>> a.pop()
44
>>> t
[66, 33]
>>> #임의의 값 t로 미리 지정해서 [66, 33]을 추출하여 사용할수도 있다
>>> a.append(9)
>>> a.append(9)
>>> 
>>> a.count(9)
3
>>> a.count(6)
2
>>> a.count(3333)
0
>>> #갯수 셀때 count
>>> 
>>> del(a[4])
>>> a
[1004, 3, 6, 80, 6, 8, 99, 77, 9, 9]
>>> a.remove(6)
>>> a
[1004, 3, 80, 6, 8, 99, 77, 9, 9]
>>> #remove가 list 함수임
>>> a.remove(9)
>>> a
[1004, 3, 80, 6, 8, 99, 77, 9]
>>> aa = a
>>> ia(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    ia(a)
NameError: name 'ia' is not defined
>>> id(a)
2311942287488
>>> id(aa)
2311942287488
>>> aaa = a.copy()
>>> aa
[1004, 3, 80, 6, 8, 99, 77, 9]
>>> a
[1004, 3, 80, 6, 8, 99, 77, 9]
>>> aaa
[1004, 3, 80, 6, 8, 99, 77, 9]
>>> 
>>> a[1] = 22
>>> a
[1004, 22, 80, 6, 8, 99, 77, 9]
>>> aa
[1004, 22, 80, 6, 8, 99, 77, 9]
>>> 
>>> aaa
[1004, 3, 80, 6, 8, 99, 77, 9]
>>> #주소값을 달리하는 동일한 데이터 만들떄는 copy
>>> 
>>> a.reverse()
>>> a
[9, 77, 99, 8, 6, 80, 22, 1004]
>>> #sort는 오름차순 정렬
>>> a.sort()
>>> a
[6, 8, 9, 22, 77, 80, 99, 1004]
>>> #내림차순 정렬도 있다. sort default 값이 flase?임
>>> #위에꺼 잘못씀. reverse 디폴트가 false임
>>> a.sort(reverse=True)
>>> a
[1004, 99, 80, 77, 22, 9, 8, 6]
>>> #del 과 remove의 차이?
>>> #remove는 하나씩 지울때.
>>> #del은 위치를 지정하여 삭제.
>>> 
>>> 
=========================== RESTART: Shell ==========================
>>> #shell 들어가서 restart shell하면 초기화됨.
>>> a = [4, 6, 5.5, 7.7, 'ace', 'korea', 3]
>>> a
[4, 6, 5.5, 7.7, 'ace', 'korea', 3]
>>> type(a)
<class 'list'>
>>> len(a)
7
>>> #sort로 정렬이 안된다!
>>> b = ['서울', '부산', '대구']
>>> b.sort()
>>> b
['대구', '부산', '서울']
>>> #같은 종류의 데이터는 정렬이 된다.
>>> 
>>> #method == 멤버함수
>>> #field  == 멤버변수
>>> #객체   == method + field
>>> 
>>> #a의 타입이 list기 떄문에 dir(list) = dir(a)는 같다.
>>> #__ 붙은게 magic method, 뒤에 오는게 멤버함수
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> #magic method = 특정 용도를 가지고 있으며, 시스템이 기본 제공
>>> #		  = object class 로부터 상속
>>> a
[4, 6, 5.5, 7.7, 'ace', 'korea', 3]
>>> b
['대구', '부산', '서울']
>>> a == b
False
>>> #컴터는 내부적으로 a == b 를 a.__eq__(b)로 해석한다
>>> 
>>> #tuple method~
>>> t = (30, 50, 70)
>>> len(t)
3
>>> t[0]
30
>>> t[1], [2]
(50, [2])
>>> t[1], t[2]
(50, 70)
>>> t.index(30)
0
>>> t.index(50)
1
>>> t.index(40)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    t.index(40)
ValueError: tuple.index(x): x not in tuple
>>> t.count(30)
1
>>> t.count(220)
0
>>> t[1] = 400
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    t[1] = 400
TypeError: 'tuple' object does not support item assignment
>>> #tuple은 변경 불가능한 list이다. (데이터 추가 불가능함)
>>> 
>>> #그래도 꼭 바꾸고 싶으면 tuple을 list로 형변환을 하면 된다.
>>> type(t)
<class 'tuple'>
>>> list(t)
[30, 50, 70]
>>> t = list(t)
>>> 
>>> t[2] = 99
>>> t
[30, 50, 99]
>>> t = tuple(t)
>>> t
(30, 50, 99)
>>> type(t)
<class 'tuple'>
>>> #형변환 한뒤에 데이터 수정후 다시 tuple로 형변환을 한다.
>>> 
>>> #[] : list 괄호/ {} : set, dict 괄호 / () : tuple 괄호
>>> 
>>> #정통적인 데이터 맞교환 방식은 아래와 같았다\
>>> i = 100
>>> j = 300
>>> i
100
>>> j
300
>>> t = i
>>> i = j
>>> j = t
>>> i
300
>>> j
100
>>> #데이터가 맞교환 되었다.
>>> 
>>> #파이썬에서는 좀더 쉽게 가능함
>>> i, j = j, i
>>> i
100
>>> j
300
>>> #정수 뿐만 아니라 문자열도 교환 가능하다.
>>> 
>>> z = 10, 20, 30
>>> z
(10, 20, 30)
>>> type(z)
<class 'tuple'>
>>> z1, z2, z3 = z
>>> z
(10, 20, 30)
>>> z1
10
>>> z2
20
>>> z3
30
>>> # z는 (10, 20, 30)의 형태로 있기 때문에 z1, z2, z3에 각각 치환되었다.
>>> 
>>> 
>>> #set은 순서가 없다.
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'i', 'j', 't', 'z', 'z1', 'z2', 'z3']
>>> #뒤에 a, b, i ~는 만든 데이터가 존재한다는것.
>>> #이것을 지우기 위해서는 아래와 같다
>>> 
>>> del a, b, i, j, t, z, z1, z2, z3
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> # 불필요한 데이터 지워진것 확인!
>>> 
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> #제어문(반복문, 조건?문) 구분해보기
>>> 
>>> #set 들어간다
>>> 
>>> a = {1, 2, 3, 4, 5}
>>> b = {2, 4, 6}
>>> type(a)
<class 'set'>
>>> a
{1, 2, 3, 4, 5}
>>> b
{2, 4, 6}
>>> #a b 합집합 유니온 U
>>> a|b
{1, 2, 3, 4, 5, 6}
>>> #a b 교집합
>>> a&b
{2, 4}
>>> 
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> a.intersection(b)
{2, 4}
>>> 
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> # 집합에서는 순서에 대한 개념x/ 그래서 에러가 뜬다
>>> 
>>> #추가는 가능하다. but 데이터 중복은 집합에서는 X.
>>> #이산수학 집합 파트랑 내용 겹침(수학 복습 철저히)
>>> 
>>> # 부분집합 = subset / 포함집합 = superset
>>> #			  확대집합
>>> 
>>> b.issubset(a)
False
>>> a.superset(b)
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'
>>> a.issuperset(b)
False
>>> 
>>> # ----------------dict-----------------
>>> d = {'이름':'강호동', '나이':51, '직업':'mc'}
>>> type(d)
<class 'dict'>
>>> d['이름']
'강호동'
>>> d['나이']
51
>>> d.ekys()
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    d.ekys()
AttributeError: 'dict' object has no attribute 'ekys'
>>> d.keys()
dict_keys(['이름', '나이', '직업'])
>>> d.values()
dict_values(['강호동', 51, 'mc'])
>>> d.items()
dict_items([('이름', '강호동'), ('나이', 51), ('직업', 'mc')])
>>> 
>>> for key, value in d.items():
	print(key, value)

	
이름 강호동
나이 51
직업 mc
>>> #위에꺼 반복해서 해보기
>>> 
>>> for i, j in d.items():
	print(i, '====>', j)

	
이름 ====> 강호동
나이 ====> 51
직업 ====> mc
>>> 
>>> dir(dict) #dict 함수 보기
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> ㅇ
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
>>> d
{'이름': '강호동', '나이': 51, '직업': 'mc'}
>>> d.update({'수입' :30})
>>> d
{'이름': '강호동', '나이': 51, '직업': 'mc', '수입': 30}
>>> d.get('수입')
30
>>> d.get('나이')
51
>>> 
>>> d.popitem()
('수입', 30)
>>> d
{'이름': '강호동', '나이': 51, '직업': 'mc'}
>>> #list의 pop과 차이가 있음 pop뒤에 item을 써줌
>>> 
>>> True & False
False
>>> True | False
True
>>> True ^ False
True
>>> True ^ True
False
#오후 강의
# for문
'''
Sum = 0

for i in range(1, 10, 1):
    Sum = Sum + i
    print('i ==>',i, 'Sum ===>',Sum)
'''
'''
Sum = 0

#for i in range(1, 101, 1):
#for i in range(2, 101, 2):
#for i in range(1, 101, 2):

for i in range(100, 0, -5):
    Sum = Sum + i
    print(' i ===> ', i, ' Sum ===> ', 'Sum')
'''
'''
for i in range(1, 7):
    if i == 3:
        #continue
        break
    print(i, end = ' ')
'''   
'''
while True: #while이 있어야 반복이 된다.
    dan = int(input(' 몇 단 출력 : '))
    if dan == 0:
        print(' 잘가세요 잘가세요')
        break

    if dan < 2 or dan > 9:
        print(' 바른 값을 입력하랑께')
        continue

    
    for i in range(1, 10): #i는 9까지
        print('{} * {} = {}'.format(dan, i, dan*i))
'''
#기본 if문
'''
if (3 < 2) or (3 == 3):
    print(' 참 '); print(' 목요일 ')    
'''
while True:
    score = int(input(' 점수 입력 : '))
    if score == 0:
        break

    if score > 100 or score < 0 :
        print(' 잘못 입력 하셨습니다.')
        continue

    if score >= 90:
        print( score, '수')
    elif score >= 90:
        print( score, '우')
    elif score >= 80:
        print( score, '미')
    elif score >= 70:
        print( score, '양')
    elif score >= 60:
        print( score, '수')
    else:
        print( score, '가')

#쉬는 시간
이순신 85 87 90
강감찬 75 80 95
한석봉 99 98 99
황진이 35 45 20
안중근 90 85 90
박문수 95 98 96
임꺽정 15 35 45
김정호 90 95 80
정몽주 90 90 95
오우석 50 45 60

###성적 처리 (내꺼)
st = []
with open('c:\\db\\ss.txt', 'r', encoding = 'utf8') as f: ##r은 읽어오겠단 의미 
    for i in range(10):
        st.append(f.readline().split()) ##라인단위로 읽어드림
        st[i][1] = int(st[i][1]) ##str ==> int형으로 변환
        st[i][2] = int(st[i][2]) ##이름과 점수 3가지 중에 점수만 정수형으로 변환.
        st[i][3] = int(st[i][3]) ## 0번째의 이름을 제외한 1,2,3번째 각각 지정.

        ## 총점, 평균 (왜안되남?)
        total = st[i][1] + st[i][2] + st[i][3]
        avg = total / 3
        st[i].append(total)
        st[i].append(avg)

##과목별 평균,반전체평균

total_kor = total_eng = total_mat = 0        

for i in range(10):
    total_kor = total_kor +st[i][1]
    total_eng = total_eng +st[i][2]
    total_mat = total_mat +st[i][3]

    avg_kor = total_kor / len(st)
    avg_eng = total_eng / len(st)
    avg_mat = total_mat / len(st)

for i in range(10):
    print(st[i])
#print tab키 누르면 평균이 각각 출력되기 때문에
#for 문에 포함되지 않고 독립적으로 총평균 1개만 출력하기 위해 따로 쓴다.
print(' 국어 평균 : {} 영어 평균 : {} 수학 평균 : {}, 반 평균 : {}'
        .format(avg_kor, avg_eng, avg_mat, (avg_kor + avg_eng + avg_mat) / 3))

#점수좀 그럴듯 하게 출력하는 방법
        
test = []

with open('c:\\db\\test.txt', 'r', encoding = 'utf8') as f:
        for i in range(10):
                test.append(f.readline().split())
                test[i][1] = int(test[i][1])
                test[i][2] = int(test[i][2])
                test[i][3] = int(test[i][3])

                total = test[i][1] + test[i][2] + test[i][3]
                avg = total / 3
                test[i].append(total)
                test[i].append(avg)

total_kor = total_eng = total_math = 0

for i in range(10):
        total_kor = total_kor + test[i][1]
        total_eng = total_eng + test[i][2]
        total_math = total_math + test[i][3]

avg_kor = total_kor / len(test)
avg_eng = total_eng / len(test)
avg_math = total_math / len(test)

print('***********  성  적  표   **************')
print('****************************************')
print(' 이름   국어   영어   수학   총점   평균')
print('****************************************')
for i in range(10):
        print('{}  {}  {}  {}  {}  {:1.f}'.format(test[i][0],
               test[i][1], test[i][2], test[i][3], test[i][4], test[i][5]))

print('****************************************\n')

print('{} | {} | {} | {:.2f}'.format(avg_kor, avg_eng, avg_math, (avg_kor + avg_eng + avg_math) / 3))


