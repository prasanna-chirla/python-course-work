Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#
#input formatting
a=input()
prasanna
a
'prasanna'
#input() by default for string
a=input('enter value:')
enter value:23
a
'23'
b=int(input('enter value:'))
enter value:24
b
24
b=float(input('enter price:'))
enter price:99.9
b
99.9
manes='prasanna lakshmi'
manes
'prasanna lakshmi'
names=input('enter')
enterprasanna lakshmi
names
'prasanna lakshmi'
names.split()
['prasanna', 'lakshmi']
names='prasanna,lakshmi'
names.split(',')
['prasanna', 'lakshmi']
course='python-java-sql'
course.split('-')
['python', 'java', 'sql']
set(couse).split('-')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    set(couse).split('-')
NameError: name 'couse' is not defined. Did you mean: 'course'?
NameError: name 'couse' is not defined. Did you mean: 'course'?
SyntaxError: invalid syntax
name=set(input('enter:')).split()
enter:prasanna lakshmi sita
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name=set(input('enter:')).split()
AttributeError: 'set' object has no attribute 'split'
name=set(input('enter:')).split())
SyntaxError: unmatched ')'
name=set(input('enter:').split())
enter:prasanna lakshmi sita
name
{'lakshmi', 'prasanna', 'sita'}
name=tuple(input('enter:').split())
enter:ram varun abhi
name
('ram', 'varun', 'abhi')
marks=input('eneter')
eneter89 99 68 98
marks
'89 99 68 98'
marks=input.split()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    marks=input.split()
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
marks=input().split()
23 55 78 99
marks
['23', '55', '78', '99']
map(int,marks)
<map object at 0x00000233C7997680>
list(map(int,marks))
[23, 55, 78, 99]
marks=list(map(int,input("enter").split()))
enter23 45 88 99
marls
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    marls
NameError: name 'marls' is not defined. Did you mean: 'marks'?
marks
[23, 45, 88, 99]
marks=set(map(int,input("enter").split()))
enter34 66 78 98
marks
{34, 66, 78, 98}
marks=tuple(map(int,input("enter").split()))
enter44 55 66 99
marks
(44, 55, 66, 99)
marks=list(map(float,input("enter").split()))
enter12.8 89.9 99.9
marks
[12.8, 89.9, 99.9]
marks=tuple(map(float,input("enter").split()))
enter55.9 77.9 88.9 99.9
marks
(55.9, 77.9, 88.9, 99.9)
marks=set(map(float,input("enter").split()))
enter44.9 55.9 77.9 88.9
marks
{88.9, 44.9, 77.9, 55.9}
#taking multiple values at same time
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,'str')
a
1
b
12.3
c
'str'
email,pass=input('enter e and p:').split()
SyntaxError: invalid syntax
email,password=input("enter mail and pass:").split()
enter mail and pass:prasanna@mail.com 1235
email
'prasanna@mail.com'
password
'1235'
name,marks=input("enter").split()
enterprasanna 100
name
'prasanna'
marks
'100'
int(marks)
100
a,b,c=list(map(int,input().split()))
12 34 45
a
12
b
34
c
45
a,b,c
(12, 34, 45)
a,b,c=tuple(map(int,input().split()))
44 55 99
a,b,c
(44, 55, 99)
status=eval(input())
True
status
True
type(ststus)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    type(ststus)
NameError: name 'ststus' is not defined. Did you mean: 'status'?
type(status)
<class 'bool'>
status=eval(input())
2+3j
ststus
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    ststus
NameError: name 'ststus' is not defined. Did you mean: 'status'?
>>> status
(2+3j)
>>> type(ststus)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    type(ststus)
NameError: name 'ststus' is not defined. Did you mean: 'status'?
>>> type(status)
<class 'complex'>
>>> status=eval(input())
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
                ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> s=eval(input())

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s=eval(input())
  File "<string>", line 0
    
SyntaxError: invalid syntax
>>> status=eval(input())
(1,2,3,4)
>>> status
(1, 2, 3, 4)
>>> status=eval(input())
[1,2,3,4]
>>> status
[1, 2, 3, 4]
>>> status=eval(input())
{1:1,2:3,4:5}
>>> staTUS
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    staTUS
NameError: name 'staTUS' is not defined. Did you mean: 'status'?
>>> status
{1: 1, 2: 3, 4: 5}
