Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string operations
s='prasanna'
s
'prasanna'
type(s)
<class 'str'>
s=''
s
''
a='prasanna'
b='chirla'
#concatenation
a+b
'prasannachirla'
#repetation
a*10
'prasannaprasannaprasannaprasannaprasannaprasannaprasannaprasannaprasannaprasanna'
x='prasanna'
y=' chirla'
x+y
'prasanna chirla'
'*'*10
'**********'
'-codg-'*5
'-codg--codg--codg--codg--codg-'
#indexing
name='prasanna'
#positive indexing
name[2]
'a'
name[5]
'n'
nmae[7]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nmae[7]
NameError: name 'nmae' is not defined
name[7]
'a'
nmae[-1]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    nmae[-1]
NameError: name 'nmae' is not defined
name[-1]
'a'
name[-3]
'n'
#+ve start form 0 and front ,-ve start from -1 and back
names="prasanna priyanka iswarya gayatri"
names
'prasanna priyanka iswarya gayatri'
names[:8]
'prasanna'
names[10:17]
'riyanka'
names[9:17]
'priyanka'
name[-7:]
'rasanna'
name[:-7]
'p'
names[:-7]
'prasanna priyanka iswarya '
names[-7:]
'gayatri'
names[::-1]
'irtayag ayrawsi aknayirp annasarp'
#reverse
names[-1:-7:-1]
'irtaya'
names[-1:-8:-1]
'irtayag'
#membership
prasanna in names
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    prasanna in names
NameError: name 'prasanna' is not defined
'prasanna' in names
True
gayatri not in names
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    gayatri not in names
NameError: name 'gayatri' is not defined
'gayatri' not in names
False
'a' in names
True
'z' in names
False
ord('a')
97
ord("A")
65
ord('p')
112
ord('S')
83
#ord-ascii value
chr('40')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    chr('40')
TypeError: 'str' object cannot be interpreted as an integer
chr(100)
'd'
chr('s')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    chr('s')
TypeError: 'str' object cannot be interpreted as an integer
#chr-if we have value chr gives the character
che(10)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    che(10)
NameError: name 'che' is not defined. Did you mean: 'chr'?
chr(10)
'\n'
sorted(names)
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'g', 'i', 'i', 'i', 'k', 'n', 'n', 'n', 'p', 'p', 'r', 'r', 'r', 'r', 's', 's', 't', 'w', 'y', 'y', 'y']
max(names)
'y'
min(names)
' '
#string methods
s='python Programming language'
s.lower()
'python programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.swapcase()
'PYTHON pROGRAMMING LANGUAGE'
#(lower to upper and upper to lower)
s.capitalize()
'Python programming language'
#(only do 1st letter capital)
s.title()
'Python Programming Language'
#(words first letter upper)
#casefold
#allignment methods
s.center(50,'-')
'-----------python Programming language------------'
s.center(30,'.')
'.python Programming language..'
s.center(40,'.')
'......python Programming language.......'
s.ljust(40,'.')
'python Programming language.............'
s.rjust(40,'.')
'.............python Programming language'
#zfill id i want 4 digit num but user enterd 3 digit not it will store as 0123 means add 0's at start
'123'.zfill(5)
'00123'
'8'.zfill(6)
'000008'
'132444445'.zfill(2)
'132444445'
#search and find methods
s.find('python')
0
s.fing('g')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.fing('g')
AttributeError: 'str' object has no attribute 'fing'. Did you mean: 'find'?
s.find('g')
10
s.find('programming')
-1
s.find('p')
0
>>> s.rfing('p')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.rfing('p')
AttributeError: 'str' object has no attribute 'rfing'. Did you mean: 'rfind'?
>>> s.rfind('p')
0
>>> s="python programming language"
>>> s.find('p)
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> s.find('p')
...        
0
>>> s.rfind('p')
...        
7
>>> s.find('z')
...        
-1
>>> s.index('p')
...        
0
>>> s.rindex('p')
...        
7
>>> s.index('z')
...        
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.replace('p','*')
...        
'*ython *rogramming language'
>>> s.replace('python','java')
...        
'java programming language'
>>> s.maketrans('aeiou','#$%^&')
...        
{97: 35, 101: 36, 105: 37, 111: 94, 117: 38}
>>> s.translate(s.maketrans('aeiou','#$%^&'))
...        
'pyth^n pr^gr#mm%ng l#ng&#g$'
>>> #encode decode
...        
