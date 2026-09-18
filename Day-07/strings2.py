Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='       hello         world           '
s.strip()
'hello         world'
s.lstrip()
'hello         world           '
s.rstrip()
'       hello         world'
s.replace(' ','')
'helloworld'
s='java-python-flask-mysql-c'
s.split('-')
['java', 'python', 'flask', 'mysql', 'c']
s.split('-',2)
['java', 'python', 'flask-mysql-c']
s.rsplit('-',2)
['java-python-flask', 'mysql', 'c']
l='''python'''
l='''python
flask
c
java
'''
l
'python\nflask\nc\njava\n'
l.splitlines()
['python', 'flask', 'c', 'java']
c=['python', 'flask', 'c', 'java']
c
['python', 'flask', 'c', 'java']
''.join(c)
'pythonflaskcjava'
' '.join(c)
'python flask c java'
'@'.join(c)
'python@flask@c@java'
'# '.join(c)
'python# flask# c# java'
'-'.join(('1','2','3'))
'1-2-3'
#tuple
'-'.join({'1','2','3'})
'2-1-3'
a='strings.py'
a.partiation('.')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.partiation('.')
AttributeError: 'str' object has no attribute 'partiation'. Did you mean: 'partition'?
a.partition('.')
('strings', '.', 'py')
#only divide into 3 parts
#left,right,middle
b='strings.py.java.c'
b,partition('.')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    b,partition('.')
NameError: name 'partition' is not defined
b.partition('.')
('strings', '.', 'py.java.c')
b.rpartition('.')
('strings.py.java', '.', 'c')
#string testing method
a='string.png'
a.startswith('str')
True
a.startswith('ast')
False
a.endswith('png')
True
a.endswith('pn')
False
'jhsjsw.13'.islower()
True
'dfgthj'.islower()
True
'Pyshh'.islower()
False
'PYTHON.13'.isupper()
True
'PYTHOn'.isupper()
False
'PYTH@#$ON2546'.isupper()
True
'tfadhiughj'.isalpha()
True
>>> 'sdgfhgju4567'.isalpha()
False
>>> 'rtyjuhk3456789'.isalnum
<built-in method isalnum of str object at 0x0000023B775C8870>
>>> 'rtyjuhk3456789'.isalnum()
True
>>> '345678'.isalnum()
True
>>> 'sdfghhj'.isalnum()
True
>>> '   '.isspace()
True
>>> '    h'.isapace()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    '    h'.isapace()
AttributeError: 'str' object has no attribute 'isapace'. Did you mean: 'isspace'?
>>> '    h'.issapace()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    '    h'.issapace()
AttributeError: 'str' object has no attribute 'issapace'. Did you mean: 'isspace'?
>>> '   h'.isspace()
False
>>> 'HLO WOR'.istitle()
False
>>> 'Hlo Wor'.istitle()
True
>>> 'HLO Wor'.istitle()
False
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> 
>>> '3456789'.isdecimal()
True
>>> 'dfghj'.isdecimal()
False
>>> '3456789'.isdigit()
True
>>> '5678.isnumeric()
SyntaxError: unterminated string literal (detected at line 1)
>>> '5678'.isnumeric()
True
