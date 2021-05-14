## 사용자 정의 함수
'''
def f1(): ## 함수 정의
    pass

def f2():
    print(' f2... ')

def f3(x):
    print(x, '가 좋아요')
    return None


def f4(x, y):
    print('{} + {} = {}'.format(x, y, x+y))

def plus(x, y):
    print('plus')
    print('{} + {} = {}'.format(x, y, x+y))

def minus(x, y):
    return x-y



f1() ## 함수 호출
f2()
print(f3(100))
f3('BTS')
f4(10, 20)
plus(1, 4)

minus(300, 200) #return x-y값이 여기에 저장(출력x)
retv = minus(300, 200) #내려온 ret값을 아래로 print함(출력o)
print(retv)

print(' 20 - 5 = ', minus(20, 5))
'''

##덧셈만 할 줄 아는 계산기
'''
def plus(x, y):
    print(' {} + {} = {}'.format(x, y, x+y))
    return None

def Add(x, y):
    return x+y

while True:
    number1 = int(input(' 첫 번째 수 : '))
    if number1 == 0:
        break
    number2 = int(input(' 두 번째 수 : '))

    plus(number1, number2)
    #print(' {} + {} = {}'.format(number1, number2, number1+number2))
    
    retv = Add(number1, number2)
    print(' {} + {} = {}'.format(number1, number2, retv))
'''

#프로그램 구조
''''
#===================함수 정의 부분
def Talk(x, y):
    print(x, '님이', y,' 번 말씀하셨다.')

def Aha(x):
    print(x, '누구나 딱 한 번 산다.')

#====================호출(출력) 부분

print(' Start ')

name = input('이름 : ')
num = int(input(' 횟수 : '))

for i in range(1, num+1): #100번 호출 하고 싶을때
    Aha(i)
    
Talk(name, num)

print(' End ')
'''

## 초간단 계산기
'''
#=====함수 정의 부분

def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return x//y
#=============호출(출력) 부분
while True:
    print(' ** 간단 계산기 **')
    n1 = int(input(' 첫 번째 수 : '))
    if n1 == 0:
        break

    #op = input(' [ + - * / ] : ')
    op = input(' [ {+} {-} {*} {/} ] : ')
     
    n2 = int(input(' 두 번째 수 : '))

    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
    elif op == '/':
        res = Div(n1, n2)
    else:
        print(op, '없는 연산입니다.')

    print(' {} {} {} = {}'.format(n1, op, n2, res))

'''

## 가변인수( 개수가 달라질 수 있다)
## 디폴트 값을 설정해 놓고, 상황에 따라 수치를
## 변경해야 하는 경우 사용 가능함.

## 예를 들어 캐릭터의 공격력과 방어력에 영향을
## 주는 요인이 여러가지 인데, 캐릭터 설정값을 디폴트(x)로 놓고
## 아이템(y), 스킬(z), 레벨(s) 따라 변수를 달리해야 하는 경우에
## 유용하게 활용 될 수 있을 것으로 예상함(거의 가능)

## 속도가 중요하기 때문에 공방 수치 변수는 많으면 게임 느려짐
## 최대한 단순한데 그럴듯한 수식이 필요함.

## 퀘스트 진행시, USER_NAME을 NPC가 출력하게 하는 상황에
## 아래 [철수&만수야 놀자]가 사용 가능함.
## 단, USER_NAME을 호출해오는 별도의 함수 설정이 선행되어야 함.(가능)

def Add1(x):
    print(x+x)

def Add2(x, y):
    print(x+y)

def Add3(x=100, y=100, z=100):
    '''나는 값을 더하는 함수다''' ##doc string
    print(' x = ', x, ' y = ', y, ' z = ',z)
    #print(x+y+z)

def Call(name = '철수'):
    print(name, '야! 놀자')

Call()
Call('만수')
Call(name='호도')

Add3(10, 20, 30)
Add3(30, 50)
Add3(10)
Add3()
Add3(z=5, x=7, y=3)
