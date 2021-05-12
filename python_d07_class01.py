print('안녕하세요')

a = [3, 5, 7]

print('킹' + 'ace')

#### 예외 처리 ####
try:
    a + 2
except (TypeError, IndexError) :
    print('미안미안')

try:
    a[2] / 0
except ZeroDivisionError as msg:
    print(msg)

print('안녕하숑')

print('*'*30)

#### 모듈 분리(계산기) ####

## 초간단 계산기

def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return x//y

while True:
    print(' ** 간단 계산기 ** ')
    print(' ===> [종료 : 0 ]')
    n1 = int(input(' 첫 번째 수 : '))
    if n1 == 0:
        break
    
    op = input(' [ +, - * / ] : ')
    
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

    print(' {}  {}  {} = {}'.format(n1, op, n2, res))



