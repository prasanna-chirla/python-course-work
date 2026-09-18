Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=list()
type(l)
<class 'list'>
l=[1,33.3,"sapra",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8j]
l
[1, 33.3, 'sapra', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+8j)]
l=[1,1,1,1]
l
[1, 1, 1, 1]
a=[1,2,3]
b=[4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a83
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a83
NameError: name 'a83' is not defined
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[566,78,45,98,55]
a
[566, 78, 45, 98, 55]
a[1]
78
a[3]
98
a[-1]
55
a[-3]
45
a
[566, 78, 45, 98, 55]
a[1:4]
[78, 45, 98]
a[::-1]
[55, 98, 45, 78, 566]
a[1::2]
[78, 98]
78 in a
True
321 in a
False
98 not in a
False
#list methods
a
[566, 78, 45, 98, 55]
max(a)
566
min(a)
45
sorted(a)
[45, 55, 78, 98, 566]
len(a)
5
a
[566, 78, 45, 98, 55]
id(a)
2299883752256
a[0]
566
a[3]
98
a[-1]
55
a[-3]
45
id(a)
2299883752256
a.append(99)
a
[566, 78, 45, 98, 55, 99]
a.append(668)
a
[566, 78, 45, 98, 55, 99, 668]
a.insert(2,890)
a
[566, 78, 890, 45, 98, 55, 99, 668]
a.insert(5,65)
a
[566, 78, 890, 45, 98, 65, 55, 99, 668]
a.extend([1,2,3,4])
a
[566, 78, 890, 45, 98, 65, 55, 99, 668, 1, 2, 3, 4]
a.pop()
4
a.pop()
3
a.pop(4)
98
a.pop(2)
890
a.pop(4)
55
a
[566, 78, 45, 65, 99, 668, 1, 2]
a.remove(990
         a
         
SyntaxError: '(' was never closed
a.remove(99)
         
a
         
[566, 78, 45, 65, 668, 1, 2]
del a[1]
         
a
         
[566, 45, 65, 668, 1, 2]
del[1:3]
         
SyntaxError: invalid syntax
del a[1:3]
         
a
         
[566, 668, 1, 2]
a.clear()
         
a
         
[]
a=[566, 78, 45, 65, 668, 1, 2]
         
a.index(45)
         
2
a.count(668)
         
1
a=[1,2,3,4]
         
b=a
         
b
         
[1, 2, 3, 4]
b.append(7)
         
b
         
[1, 2, 3, 4, 7]
a
         
[1, 2, 3, 4, 7]
c=a.copy()
         
c.append(12)
         
c
         
[1, 2, 3, 4, 7, 12]
>>> a
...          
[1, 2, 3, 4, 7]
>>> any([1,False,(),'',{}])
...          
True
>>> any([0,False,(),'',{}])
...          
False
>>> all([1,False,(),'',{}])
...          
False
>>> any([1,2,3,4])
...          
True
>>> all([1,2,3,4])
...          
True
>>> sum(a)
...          
17
>>> sorted(a)
...          
[1, 2, 3, 4, 7]
>>> a.sort(a)
...          
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.sort(a)
TypeError: sort() takes no positional arguments
>>> a.reverse(a)
...          
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.reverse(a)
TypeError: list.reverse() takes no arguments (1 given)
>>> a.reverse()
...          
>>> a
...          
[7, 4, 3, 2, 1]
>>> a.sort()
...          
>>> a
...          
[1, 2, 3, 4, 7]
