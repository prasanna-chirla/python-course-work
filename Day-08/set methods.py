Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
type(s)
<class 'set'>
s={1,2,3,4,5,54,765,8765}
s
{1, 2, 3, 4, 5, 765, 54, 8765}
s={1,1,1,1,1,1}
s
{1}
s=set()
s.add(1)
s.add(12.3)
s.add('str')
s
{1, 12.3, 'str'}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
#only immutable elements are allowed inside a setr
s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add({1:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(False)
s
{False, 1, 12.3, 'str'}
#operations
a={1,2,3,4,5}
b={4,5,6,7,8}
2 in a
True
10 not in a
True
a|b
{1, 2, 3, 4, 5, 6, 7, 8}
a&b
{4, 5}
a-b
{1, 2, 3}
b-a
{8, 6, 7}
a^b
{1, 2, 3, 6, 7, 8}
a
{1, 2, 3, 4, 5}
#sub set
{1}<=a
True
{1,2}<=a
True
{12}<=a
False
{1,2}>=a
False
a>={1,2}
True
a>={4}
True
a>={14,15}
False
#superset
m={12,32,43}
n={4,2,5}
a.isdisjoint(b)
False
m.isdisjoint(n)
True
#no common elemnts between two sets
#methods
a={1,2,45,67,99,87}
sorted(a)
[1, 2, 45, 67, 87, 99]
max(a)
99
\
min(a)
1
len(a)
6
a.index(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
all({1,1,23,43,13,1})
True
any({1,0})
True
any({0,''})
False
sum(a)
301
a
{1, 2, 67, 99, 87, 45}
a={1,2,3}
a
{1, 2, 3}
b={4,5,6}
b
{4, 5, 6}
b.add(9)
a
{1, 2, 3}
a=b
b.add(9)
a
{9, 4, 5, 6}
b
{9, 4, 5, 6}
c=a.copy()
c={99,88,77}
c=a.copy()
c.add(66)
c
{66, 4, 5, 6, 9}
a
{9, 4, 5, 6}
a.add(1000
      a
      
SyntaxError: '(' was never closed
a.add(100)
      
a
      
{100, 4, 5, 6, 9}
a.add(567890)
      
a
      
{100, 4, 5, 6, 9, 567890}
a.update({232345,23456,87654,43567})
      

a
      
{23456, 100, 4, 5, 6, 87654, 9, 43567, 567890, 232345}
>>> a.pop()
...       
23456
>>> a.pop()
...       
100
>>> a.remove(6)
...       
>>> a
...       
{4, 5, 87654, 9, 43567, 567890, 232345}
>>> a.remove(9)
...       
>>> a
...       
{4, 5, 87654, 43567, 567890, 232345}
>>> a.remove(87654)
...       
>>> 
>>> a
...       
{4, 5, 43567, 567890, 232345}
>>> a.remove(63526798765)
...       
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.remove(63526798765)
KeyError: 63526798765
>>> a.discard(100)
...       
>>> a
...       
{4, 5, 43567, 567890, 232345}
>>> a.discard(6)
...       
>>> a
...       
{4, 5, 43567, 567890, 232345}
>>> #discard doesnt throw erroe
...       
>>> a.clear()
...       
>>> a
...       
set()
