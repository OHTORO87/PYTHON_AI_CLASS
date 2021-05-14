Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("안녕하세요\n안녕하세요")
안녕하세요
안녕하세요
>>> print("안녕하세요\t안녕하세요")
안녕하세요	안녕하세요
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(a)
NameError: name 'a' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> input()
100
'100'
>>> a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> input()
100
'100'
>>> type(int)
<class 'type'>
>>> 100
100
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> city=input('어디서 오셨나요:')
어디서 오셨나요: 부산시
>>> city
' 부산시'
>>> a=float(input('실수 입력 :'))
실수 입력 : 20.5478
>>> a
20.5478
>>> print(a,city)
20.5478  부산시
>>> 
>>> 
>>> print('aa\t bb\t cc\n dd\t ee\a ff\b gg')
aa	 bb	 cc
 dd	 ee ff gg
>>> 
>>> print("서울은 좁아ㅏ요""아주 좁아요"'정말 좁아요')
서울은 좁아ㅏ요아주 좁아요정말 좁아요
>>> print("서울은 좁아요\t\t""아주 좁아요\n"'정말 좁아요')
서울은 좁아요		아주 좁아요
정말 좁아요
>>> age=20
>>> name='빌게이츠'
>>> print(name,'님은',age,'살')
빌게이츠 님은 20 살
>>> print('%s, %d'%(name, age))
빌게이츠, 20
>>> print(' [%d] [%10d] [%-10d]' %(5, 5, 5))
 [5] [         5] [5         ]
>>> print(' {}{}'.format(10, ' seoul'))
 10 seoul
>>> print(' {}{}'.format(10, 3.14, ' seoul'))
 103.14
>>> print(' {}{}{}'.format(10, 3.14, ' seoul'))
 103.14 seoul
>>> print(' {} {} {}'.format(10, 3.14, 'seoul'))
 10 3.14 seoul
>>> print(' {0} {1} {2}'.format(10, 3.14, 'seoul'))
 10 3.14 seoul
>>> print(' {1} {0} {2}'.format(10, 3.14, 'seoul'))
 3.14 10 seoul
>>> print(' {1} {1} {1}'.format(10, 3.14, 'seoul'))
 3.14 3.14 3.14
>>> print(' [{1}] [{1}] [{1}]'.format(10, 3.14, 'seoul'))
 [3.14] [3.14] [3.14]
>>> print(' [{:20}] [{:10}] [{:20}]'.format(10, 3.14, 'seoul'))
 [                  10] [      3.14] [seoul               ]
>>> print(' [{:>20}] [{:>10}] [{:<20}]'.format(10, 3.14, 'seoul'))
 [                  10] [      3.14] [seoul               ]
>>> print(' [{:<20}] [{:<10}] [{:>20}]'.format(10, 3.14, 'seoul'))
 [10                  ] [3.14      ] [               seoul]
>>> print(' [{:<20}] [{:^10}] [{:>20}]'.format(10, 3.14, 'seoul'))
 [10                  ] [   3.14   ] [               seoul]
>>> print(' [{:<20}] [{:%f}] [{:>20}]'.format(10, 3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(' [{:<20}] [{:%f}] [{:>20}]'.format(10, 3.14, 'seoul'))
ValueError: Invalid format specifier
>>> 
>>> print(' [{:<20}] [{:2f}] [{:>20}]'.format(10, 3.14, 'seoul'))
 [10                  ] [3.140000] [               seoul]
>>> #위에껀 잘못된거임
>>> print(' [{:<20}] [{:10f}] [{:>20}]'.format(10, 3.14, 'seoul'))
 [10                  ] [  3.140000] [               seoul]
>>> #10f = 소수점이하 10번째까지 출력해~
>>> 
>>> print(' %f, %.2f, %.10f'.format(2.13, 2.13, 2.13))
 %f, %.2f, %.10f
>>> print(' {%f}, {%.2f}, {%.10f}'.format(2.13, 2.13, 2.13))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(' {%f}, {%.2f}, {%.10f}'.format(2.13, 2.13, 2.13))
KeyError: '%f'
>>> print(' {%f}, {%.2f}, {%.10f}'%(2.13, 2.13, 2.13))
 {2.130000}, {2.13}, {2.1300000000}
>>> print(' %f, %.2f, %.10f'%(2.13, 2.13, 2.13))
 2.130000, 2.13, 2.1300000000
>>> #그냥하면 소수점 6자리까지
>>> # %f = 디폴트값이 소수점 6자리??
>>> Sum = 0
>>> range(10)
range(0, 10)
>>> range(1, 11)
range(1, 11)
>>> for i in range(0, 10):
	print(i, end='/n')

	
0/n1/n2/n3/n4/n5/n6/n7/n8/n9/n
>>> 
>>> for i in range(10):
	print(i)
	range(10)

	
0
range(0, 10)
1
range(0, 10)
2
range(0, 10)
3
range(0, 10)
4
range(0, 10)
5
range(0, 10)
6
range(0, 10)
7
range(0, 10)
8
range(0, 10)
9
range(0, 10)
>>> for i on range(10):
	
SyntaxError: invalid syntax
>>> 
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0, 10):
	print(i, end-'\n')

	
Traceback (most recent call last):
  File "<pyshell#74>", line 2, in <module>
    print(i, end-'\n')
NameError: name 'end' is not defined
>>> for i in range(0, 10):
	print(i, end='\n')

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1, 100, 5):
	print(i, end= '  ')

	
1  6  11  16  21  26  31  36  41  46  51  56  61  66  71  76  81  86  91  96  
>>> for i in range(5, 100, 4):
	print(i, end='\t')

	
5	9	13	17	21	25	29	33	37	41	45	49	53	57	61	65	69	73	77	81	85	89	93	97	
>>> Sum=0
>>> for i in range(1,11):
	Sum = Sum + i

	
>>> Sum
55
>>> for i in range(1, 101):
	Sum = Sum +i

	
>>> print(Sum)
5105
>>> Sum = 0
>>> for i in range(1, 101):
	Sum = Sum +i

	
>>> Sum
5050
>>> for i in range(1, 101, 2):
	Sum = Sum +i

	
>>> Sum
7550
>>> 
>>> Sum2 = 0.0
>>> for i in range(100):
	Sum = Sum +0.1

	
>>> for i in range(100):
	Sum2 = Sum2 +0.1

	
>>> Sum2
9.99999999999998
>>> print('[%f]'%(Sum2))
[10.000000]
>>> print('[%.30f]%(Sum2))
      
SyntaxError: EOL while scanning string literal
>>> print('[%.30f]'%(Sum2))
[9.999999999999980460074766597245]
>>> print('[%.3f]'%(Sum2))
[10.000]
>>> 
>>> 
>>> a = int(input('정수 : '))
정수 : 30
>>> b = int(input('정수 : '))
정수 : 50
>>> 
>>> print(a, b, a+b)
30 50 80
>>> #한번에 정수 2개 값을 입력 할 수도 있다
>>> a, b = input().split()
30 50
>>> a, b
('30', '50')
>>> c, d = input().split()
10, 20
>>> c, d
('10,', '20')
>>> 
>>> 
>>> #메모장 불러오는법??
>>> 
>>> f = open('c:\\db\\aa.txt', 'r', encording='utp8')
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    f = open('c:\\db\\aa.txt', 'r', encording='utp8')
TypeError: 'encording' is an invalid keyword argument for open()
>>> f = open('c:\\db\\aa.txt', 'r', encoding='utp8')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    f = open('c:\\db\\aa.txt', 'r', encoding='utp8')
LookupError: unknown encoding: utp8
>>> f = open('c:\\db\\aa.txt', 'r', encoding='utf8')
>>> print(f.read)
<built-in method read of _io.TextIOWrapper object at 0x0000020411C97AD0>
>>> print(f.read())
오늘은 화요일
비가 옵니다.
내일은 수요일
어린이날 입니다.
나에게 키보드를 선물합니다.
>>> #파이썬에서 글써서 메모장에 입력 되도록 하는법
>>> 
>>> f2 = open('c:\\db\\bb.txt', 'w', encoding='utf8')
>>> f2.write('파이썬에 글을 써보자')
11
>>> f2.write('파이썬에서 메모장에 글을 입력한다는게 사실일까?')
26
>>> f.close()
>>> f2.close()
>>> f2.write('파이썬에서 메모장에 글을 입력한다는게 사실일까?/n')
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    f2.write('파이썬에서 메모장에 글을 입력한다는게 사실일까?/n')
ValueError: I/O operation on closed file.
>>> f2.write('파이썬에서 메모장에 글을 입력한다는게 사실일까?\n')
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    f2.write('파이썬에서 메모장에 글을 입력한다는게 사실일까?\n')
ValueError: I/O operation on closed file.
>>> f2.open()
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    f2.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> f.open()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    f.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> f = open('c:\\db\\bb.txt', 'w', encoding='utp8')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    f = open('c:\\db\\bb.txt', 'w', encoding='utp8')
LookupError: unknown encoding: utp8
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utp8')
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    f = open('c:\\db\\bb.txt', 'a', encoding='utp8')
LookupError: unknown encoding: utp8
>>> f.close()
>>> f2.close()
>>> f2 = open('c:\\db\\bb.txt', 'w', encoding='utf8')
>>> f2.write('파이썬은 짱입니다. \n')
12
>>> f2('위의 말은 사실입니다. \n')
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    f2('위의 말은 사실입니다. \n')
TypeError: '_io.TextIOWrapper' object is not callable
>>> f2.write('위의 말은 사실입니다. \n')
14
>>> f.close()
>>> f2.close()
>>> f3 = open('c:\\db\\bb.txt', 'a', encoding='utp8')
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    f3 = open('c:\\db\\bb.txt', 'a', encoding='utp8')
LookupError: unknown encoding: utp8
>>> f3 = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	name = input('친구 이름: ')
	f3.write(name)

	
친구 이름: 이승만
3
친구 이름: 박정희
3
친구 이름: 전두환
3
친구 이름: 노태우
3
친구 이름: 김영삼
3
>>> f3.close()
>>> 
>>> 
>>> #형변환!!
>>> int(a)
30
>>> a=100
>>> int(a)
100
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : ')
	f.write(life)

	
생사 여부 : 사망
2
생사 여부 : 사망
2
생사 여부 : 생존
2
생사 여부 : 생존
2
생사 여부 : 사망
2
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')for i in range(5):
	life = input('생사 여부 : \n')
	f.write(life)
	
SyntaxError: invalid syntax
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : \n')
	f.write(life)

	
생사 여부 : 
사망
2
생사 여부 : 
사망
2
생사 여부 : 
생존
2
생사 여부 : 
생존
2
생사 여부 : 
사망
2
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : \n')
	f.write(life/n)

	
생사 여부 : 
사망
Traceback (most recent call last):
  File "<pyshell#177>", line 3, in <module>
    f.write(life/n)
NameError: name 'n' is not defined
>>> 사망
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    사망
NameError: name '사망' is not defined
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : \n')
	f.write(life /n)

	
생사 여부 : 
사망
Traceback (most recent call last):
  File "<pyshell#181>", line 3, in <module>
    f.write(life /n)
NameError: name 'n' is not defined
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : \n')
	f.write(life '/n')
	
SyntaxError: invalid syntax
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')for i in range(5):
	life = input('생사 여부 : \n')
	f.write(life)
	
SyntaxError: invalid syntax
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : ')
	f.write(life)

	
생사 여부 : 사망 \n
5
생사 여부 : 사망 \n
5
생사 여부 : 생존 \n
5
생사 여부 : 생존 \n
5
생사 여부 : 사망 \n
5
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : ''/n')
	f.write(life)

	
생사 여부 : /n사망
2
생사 여부 : /n사망
2
생사 여부 : /n사망
2
생사 여부 : /n사망
2
생사 여부 : /n사망
2
>>> f.clsoe()
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    f.clsoe()
AttributeError: '_io.TextIOWrapper' object has no attribute 'clsoe'
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 :  /n')
	f.write(life)

	
생사 여부 :  /n사망
2
생사 여부 :  /n마삼
2
생사 여부 :  /n마사
2
생사 여부 :  /n마사
2
생사 여부 :  /n사망
2
>>> 
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 :  /n')
	f.write('life \n')

	
생사 여부 :  /n사망
6
생사 여부 :  /n사망
6
생사 여부 :  /n사망
6
생사 여부 :  /n사망
6
생사 여부 :  /n사망
6
>>> 
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : ')
	f.write('life \n')

	
생사 여부 : 12
6
생사 여부 : 12
6
생사 여부 : 12
6
생사 여부 : 12
6
생사 여부 : 12
6
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x0000020411C97AD0>
>>> f.close()
>>> f = open('c:\\db\\bb.txt', 'a', encoding='utf8')
>>> for i in range(5):
	life = input('생사 여부 : ')
	f.write('life \n')

	
생사 여부 : 다다
6
생사 여부 : 다라
6
생사 여부 : 라나
6
생사 여부 : 나나
6
생사 여부 : 카다
6
>>> 
>>> f.close()
>>> 
>>> 
>>> f.close()
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> Chr('a')
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    Chr('a')
NameError: name 'Chr' is not defined
>>> chr(ord)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    chr(ord)
TypeError: an integer is required (got type builtin_function_or_method)
>>> chrord
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    chrord
NameError: name 'chrord' is not defined
>>> chr.ord
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    chr.ord
AttributeError: 'builtin_function_or_method' object has no attribute 'ord'
>>> chr
<built-in function chr>
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> chr
<built-in function chr>
>>> chr(65)
'A'
>>> ord('a')
97
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 3 in a
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    3 in a
TypeError: argument of type 'int' is not iterable
>>> k1 =30
>>> k2 = 20
>>> k3= 30
>>> k1 is k3
True
>>> k1 is k2
False
>>> k1 is 30
True
>>> id(30)
2216499571920
>>> k2 is not 30
True
>>> 3 not in a
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    3 not in a
TypeError: argument of type 'int' is not iterable
>>> 30 not in k1
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    30 not in k1
TypeError: argument of type 'int' is not iterable
>>> 3<3
False
>>> 3<=3
True
>>> 3<=3 and 4==5
False
>>> 3<=3 or 4==4
True
>>> 3+2*3
9
>>> #가독성이 높은 코드가 좋은 코드
>>> a=(1,2,3,4,5)
>>> sd(a)
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    sd(a)
NameError: name 'sd' is not defined
>>> mean(a)
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    mean(a)
NameError: name 'mean' is not defined
>>> var(a)
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    var(a)
NameError: name 'var' is not defined
>>> median(a)
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    median(a)
NameError: name 'median' is not defined
>>> 3 in a
True
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> chr(ord('a'))
'a'
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> print(chr('a'))
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    print(chr('a'))
TypeError: an integer is required (got type str)
>>> ord('a')
97
>>> ord('A')
65
>>> chr('65')
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    chr('65')
TypeError: an integer is required (got type str)
>>> chr(65)
'A'
>>> chr(99)
'c'
>>> ord('r')
114
>>> chr(114)
'r'
>>> str(1000)
'1000'
>>> int('3333')
3333
>>> #이것이 형변환 함수다! str int ; 데이터의 형태를 바꾼다
>>> int('30')
30
>>> str('22')
'22'
>>> float(45)
45.0
>>> float('국민')
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    float('국민')
ValueError: could not convert string to float: '국민'
>>> int(국민)
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    int(국민)
NameError: name '국민' is not defined
>>> a=[2,4,6,8,10]
>>> b=(1,2,3)
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> sum(a)
30
>>> sum(b)
6
>>> max(a)
10
>>> min(a)
2
>>> max(b)
3
>>> min(b)
1
>>> mean(a)
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    mean(a)
NameError: name 'mean' is not defined
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> #a와 연관이 있는 함수를 보고 싶을떄!!! dir
>>> 
>>> #dir = 마법의 method = 멤버함수
>>> #dir(a) 해서 나오는게 멤버함수!! 특수한 용도가 있는디~
>>> #무슨 용도일까? => 나중에 알려드릴꼐
>>> 
>>> k=20
>>> dir(k)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> #k가 정수 이기 떄문에 int를 입력해도 같은 내용이 출력된다!!
>>> k+30
50
>>> k.__add__(30)
50
>>> #위는 우리가 쓰는거고, 아래는 실제 컴퓨터가 수행하는 방법
>>> k==60
False
>>> k.__eq__(60)
False
>>> k!=60
True
>>> k.__ne__(60)
True
>>> #__ne__는 낫이퀄이고 __neg__는 네거티브일텐데 어케 다른지 아직 모름
>>> #코딩할때 '가독성'을 높히기 위해 공백을 쓰는 습관을 들여라.
>>> 
