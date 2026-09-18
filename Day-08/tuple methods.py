Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
t=(1,2,3,4)
t
(1, 2, 3, 4)
t=(1)
t
1
t=(1,)
t
(1,)
t=(1,1,1,1)
t
(1, 1, 1, 1)
type(t)
<class 'tuple'>
#operations
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t=(1,23.4,'str',[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[2]
'str'
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t[-1]
True
t[::-1]
(True, {1: 1, 2: 2}, {1, 2, 3}, (1, 2, 3), [1, 23], 'str', 23.4, 1)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[:-2:-1]
(True,)
t[-1:-3:-1]
(True, {1: 1, 2: 2})
t[:-3:-1]
(True, {1: 1, 2: 2})
23.4 in t
True
9 in t
False
True not in t
False
sorted(t)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t=(1,2,34,5,6,89,55,77,89,456,7654)
t
(1, 2, 34, 5, 6, 89, 55, 77, 89, 456, 7654)
sorted(t)
[1, 2, 5, 6, 34, 55, 77, 89, 89, 456, 7654]
max(t)
7654
min(t)
1
len(t)
11
count(t)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    count(t)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> count(89)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    count(89)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> t.count(89)
2
>>> t.index(32)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t.index(32)
ValueError: tuple.index(x): x not in tuple
>>> t.index(6)
4
>>> sum(t)
8468
>>> all((1,2,3))
True
>>> any((1,2,3,0,00))
True
>>> all((1,2,3,0,00))
False
>>> t=1,2,3
>>> t
(1, 2, 3)
>>> a,b,c=t
>>> a
1
>>> b
2
>>> c
3
>>> t=(1,2,3,4,[1,2],5)
>>> t[4]
[1, 2]
>>> t[4].append(5)
>>> t
(1, 2, 3, 4, [1, 2, 5], 5)
>>> t.append(10)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t.append(10)
AttributeError: 'tuple' object has no attribute 'append'
>>> #we can onlu append in list which is taken in tuple but not to tuple directly
