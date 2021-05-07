## C포인터의 개념과 같은?
## 개별값이 넘어가는 것과 주소가 넘어가는것의 차이는 무엇인가?
## 빌트인 함수명은 허용되나 사용하면 안된다.

'''
def SUM(x):
    s = 0
    for i in x:
        s = s + 1
    return s

def SUM100(*x):
    s = 0
    for i in x:
        s = s + i
    return s

a = [3, 6, 9]

print(SUM(a))
print(SUM([1, 2, 3, 4, 5, 6]))
print(SUM100(*a))
'''

## dict 함수
## list는 0번쨰 1번째 2번쨰 이렇게 데이터를 주는데
## dict은 형태는 같지만, 문자열로 데이터를 준다.?

'''
color = {'black':'검정', 'yellow':'노랑', 'blue':'파랑'}

def disp_color(**x):
'''
## **x의 뜻은 사전형 데이터를 받겠다는 뜻.
'''
    for key, value in x.items():
        print(key, value)
    print(x['black'], x['yellow'], x['blue'])

disp_color(**color)

'''

## 전역 변수 지역변수
## gg값 이 전역과 지역으로 나뉘었을때는
## 서로 영향이 없다.

## 하지만 지역변수 gg 앞에 global을 쓰면
## 지역변수 gg의 값이 전역변수에 영향을 준다.

'''
gg =500  ## 전역변수

def f1(x):
    global gg  ## 전역변수 gg를 뜻함 
    gg = 2000000  ## 지역변수
    print(gg, ' x ==> ', x*x)

def f2(x, y):
    t = x*y  ## t는 지역변수, f2함수내에서만 통용된다.
    print(t)

print(f1(100))
print(f2(100, 300))
'''

## 일회용 함수(lambda 함수)

lambda x: x*x
f = lambda x: x*x
f(10)

## 파이썬은 모든것을 객체로 취급한다.
## 정수, 실수, 리스트, 함수, 클래스,,,,

a2 = [ i for i in range(1, 11) ]
>>> a2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## 위에꺼를...comprehension 이라고함
>>> a2 = list(range(1, 11))
>>> a2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> [ i for i in range(1, 11) ]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a2  = [ i for i in range(1, 11) ]
>>> a2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> list(map(lambda x: x*x, range(1, 11)))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> fff = lambda x:x*x
>>> 
>>> list(map(fff, range{1, 11)))
SyntaxError: invalid syntax
>>> list(map(fff, range(1, 11)))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



