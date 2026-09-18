Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictonaries
#mut ord het dyn unidu
d={}
type(d)
<class 'dict'>
d={1:4,2:8,3:13}
d
{1: 4, 2: 8, 3: 13}
d={}
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,4)]=1
d[(2+3j)]=1
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d={1:1,12.3:1,'str':1,(1,2,4):1,(2+3j):1}
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
d[False]=1
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1}
d[1]=1
d[2]=12.3
d[3]='str'
d[4]=2+3j
d[5]=True
d[6]=[1,2,3]
d[7]=(1,2,3)
d[8]={1,2,3}
d[9]=frozenset({1,2,3})
d[10]={1:1,2:2}
d[11]=None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
d={}
d
{}
d[1]=2
d
{1: 2}
d[1]=3
d
{1: 3}
#dictonary operations
data={'name':'prasanna','course':'pfs','batch':65)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
data={'name':'prasanna','course':'pfs','batch':65}
data
{'name': 'prasanna', 'course': 'pfs', 'batch': 65}
'prasanna' in data
False
\
'course' in data
True
data.get('name')
'prasanna'
data.get('batch')
65
data.get('age')
data.get('age','key is not present')
'key is not present'
data.get('batch','key is not present')
65
data
{'name': 'prasanna', 'course': 'pfs', 'batch': 65}
data['age']=21
d
{1: 3}
data['phno']=234567890
data
{'name': 'prasanna', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 234567890}
data.update({'email':'dfghj@gmail.com','py':2026})
data
{'name': 'prasanna', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2026}
id(data)
1665445764096
data['py']
2026
data['py']=2027
data
{'name': 'prasanna', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2027}
data['age']=22
id(data)
1665445764096
data.popitem()
('py', 2027)
data.pop('course')
'pfs'
data
{'name': 'prasanna', 'batch': 65, 'age': 22, 'phno': 234567890, 'email': 'dfghj@gmail.com'}
data.pop('age')
22
data
{'name': 'prasanna', 'batch': 65, 'phno': 234567890, 'email': 'dfghj@gmail.com'}
data.clear()
data
{}
data={'name': 'prasanna', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2027}
del data['batch']
data
{'name': 'prasanna', 'course': 'pfs', 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2027}
len(data)
6
>>> data.keys()
dict_keys(['name', 'course', 'age', 'phno', 'email', 'py'])
>>> data.values()
dict_values(['prasanna', 'pfs', 21, 234567890, 'dfghj@gmail.com', 2027])
>>> sorted(data)
['age', 'course', 'email', 'name', 'phno', 'py']
>>> max(data)
'py'
>>> min(data)
'age'
>>> data.itema()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    data.itema()
AttributeError: 'dict' object has no attribute 'itema'. Did you mean: 'items'?
>>> data.items()
dict_items([('name', 'prasanna'), ('course', 'pfs'), ('age', 21), ('phno', 234567890), ('email', 'dfghj@gmail.com'), ('py', 2027)])
>>> d={1:1,2:2}
>>> m=d
>>> m[3]=3
>>> d
{1: 1, 2: 2, 3: 3}
>>> m
{1: 1, 2: 2, 3: 3}
>>> n=d.copy()
>>> n[4]=4
>>> n
{1: 1, 2: 2, 3: 3, 4: 4}
>>> d
{1: 1, 2: 2, 3: 3}
>>> data
{'name': 'prasanna', 'course': 'pfs', 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2027}
>>> data.get('py')
2027
>>> data.get('id')
>>> data.setdefault('id',2026)
2026
>>> data
{'name': 'prasanna', 'course': 'pfs', 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2027, 'id': 2026}\
>>> data.setdefault('name',2026)
'prasanna'
>>> data
{'name': 'prasanna', 'course': 'pfs', 'age': 21, 'phno': 234567890, 'email': 'dfghj@gmail.com', 'py': 2027, 'id': 2026}
>>> dict.fromkeys({"python","java","c"},0)
{'java': 0, 'c': 0, 'python': 0}
