Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
#int floar complex
a=12
type(a)
<class 'int'>
b=13.4
type(b)
<class 'float'>
c=12+4j
type(C)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
type(c)
<class 'complex'>
#str list tuple
s='codegnan'
id(s)
3010014830192
s+='python'
id(s)
3010014787696
>>> type(s)
<class 'str'>
>>> l=[1,2,3,3,e]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l=[1,2,3,3,e]
NameError: name 'e' is not defined
>>> l=[1,2,1,2]
>>> type(l)
<class 'list'>
>>> id(l)
3010014829376
>>> l.append(12)
>>> l
[1, 2, 1, 2, 12]
>>> id(l)
3010014829376
>>> l=[1,12.3,'str',[1,2])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l=[1,12.3,'str',[1,2])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l=[1,12.3,'str',[1,2]]
>>> t=(1,2,3,4)
>>> type(t)
<class 'tuple'>
>>> s={2,4,5,7,9,0}
>>> s={2,4,5,7,9,0}id(s)
SyntaxError: invalid syntax
>>> id(s)
3010014371776
>>> s.add(20)
>>> id(s)
3010014371776
>>> a={1,12.3,'str'}
>>> a
{1, 12.3, 'str'}
>>> d={'name':'rws','price':33,'stock':True}
>>> d
{'name': 'rws', 'price': 33, 'stock': True}
>>> s=frozenset({1,5,3,9})
>>> a=True
>>> b=True
>>> type(a)
<class 'bool'>
>>> a={}
>>> j=[]
s=''
s=None
type(s)
<class 'NoneType'>
