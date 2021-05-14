Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k = "korea"
>>> type(k)
<class 'str'>
>>> k[0]
'k'
>>> k[1]
'o'
>>> k[2]
'r'
>>> k[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    k[5]
IndexError: string index out of range
>>> k[-1]
'a'
>>> k[-2]
'e'
>>> k[-5]
'k'
>>> k
'korea'
>>> k.find('k')
0
>>> k.find('o')
1
>>> k.find('T')
-1
>>> k.find('k')
0
>>> k2 = k * 3
>>> k2
'koreakoreakorea'
>>> k2.find('a)
	
SyntaxError: EOL while scanning string literal
>>> k2.rfind('a')
14
>>> k2.count('a')
3
>>> k2.rfind('k')
10
>>> k2.rfind('o'0
	 
SyntaxError: invalid syntax
>>> k2.rfind('o')
11
>>> k2.count('R')
0
>>> k2.startswitch('R')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    k2.startswitch('R')
AttributeError: 'str' object has no attribute 'startswitch'
>>> k2.startswitch('k')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    k2.startswitch('k')
AttributeError: 'str' object has no attribute 'startswitch'
>>> k2.startswitch('p')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    k2.startswitch('p')
AttributeError: 'str' object has no attribute 'startswitch'
>>> k2.endswitch('a')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    k2.endswitch('a')
AttributeError: 'str' object has no attribute 'endswitch'
>>> k2.endswitch('b')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    k2.endswitch('b')
AttributeError: 'str' object has no attribute 'endswitch'
>>> k2
'koreakoreakorea'
>>> 
>>> k2.upper()
'KOREAKOREAKOREA'
>>> k2
'koreakoreakorea'
>>> k3 = k2.upper()
>>> k3
'KOREAKOREAKOREA'
>>> k3.lower()
'koreakoreakorea'
>>> s = ' seoul '
>>> s
' seoul '
>>> k
'korea'
>>> k2
'koreakoreakorea'
>>> len(k)
5
>>> k2
'koreakoreakorea'
>>> len(k)
5
>>> len(k2)
15
>>> len(s)
7
>>> s.strip()
'seoul'
>>> s.lstrip()
'seoul '
>>> s.rstrip()
' seoul'
>>> 'T'.isalpha()
True
>>> '0'.isalpha()
False
>>> '5'.isalpha()
False
>>> '$'.isalpha()
False
>>> '7
SyntaxError: EOL while scanning string literal
>>> '7'.isnumeric()
True
>>> '$'.isnumeric()
False
>>> 'A'.isnumeric()
False
>>> 'A'.isalnum()
True
>>> '6'.isalnum()
True
>>> s = "seoul"
>>> 
>>> print(s, "가 좋아요")
seoul 가 좋아요
>>> s.replace('e', 'E')
'sEoul'
>>> S
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
'seoul'
>>> k2.startswith('R')
False
>>> k2.startswith('s')
False
>>> k2.startswith('k')
True
>>> 
>>> print(s, "가 좋아요")
seoul 가 좋아요
>>> s.replace('e', 'E')
'sEoul'
>>> s
'seoul'
>>> b1 = "서울이 좋아요"
>>> b2 =
SyntaxError: invalid syntax
>>> b2 = b1.replace("서울", "부산")
>>> b1, b2
('서울이 좋아요', '부산이 좋아요')
>>> b1
'서울이 좋아요'
>>> b2
'부산이 좋아요'
>>> 
>>> bc = "kbs mbc sbs ebs ytn"
>>> bc
'kbs mbc sbs ebs ytn'
>>> bc2 = bc.upper()
>>> bc2
'KBS MBC SBS EBS YTN'
>>> type(bc)
<class 'str'>
>>> type(bc2)
<class 'str'>
>>> bc3 = bc2.split()
>>> bc3
['KBS', 'MBC', 'SBS', 'EBS', 'YTN']
>>> type(bc3), len(bc3)
(<class 'list'>, 5)
>>> bc4 = "kbs/mbc/sbs"
>>> bc4
'kbs/mbc/sbs'
>>> bc5 = bc4.split('/')
>>> bc5
['kbs', 'mbc', 'sbs']
>>> bc4 = "kbs:mbc:sbs"
>>> bc4
'kbs:mbc:sbs'
>>> bc5 = bc4.split(':')
>>> bc5
['kbs', 'mbc', 'sbs']
>>> a = apple
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a = apple
NameError: name 'apple' is not defined
>>> dir(a)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    dir(a)
NameError: name 'a' is not defined
>>> a= 4
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> b=3
>>> dir(b)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> b = 'rea'
>>> dir(b)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> a = apple
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a = apple
NameError: name 'apple' is not defined
>>> a = 'apple'
>>> a +4
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a +4
TypeError: can only concatenate str (not "int") to str
>>> a*3
'appleappleapple'
>>> b = "banana"
>>> b
'banana'
>>> a + b
'applebanana'
>>> b * 4
'bananabananabananabanana'
>>> Sum
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    Sum
NameError: name 'Sum' is not defined
>>> a
'apple'
>>> b
'banana'
>>> c
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> apple = True;
>>> orange = False;
>>> orange
False
>>> apple
True
>>> type(apple)
<class 'bool'>
>>> type(orange)
<class 'bool'>
>>> orange and apple
False
>>> not orange
True
>>> apple and not orange
True
>>> not apple
False
>>> not apple and orange
False
>>> apple or orange
True
>>> #bool은 참과 거짓 값 또는 그런 값을 가지는 형태를 말함
