Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operators
#arithematic operators
a=10
b=5
a+b
15
a-b
5
a*b
50
a*8
80
a/2
5.0
a//2
5
10.2//2
5.0
a**3
1000
2**3
8
#comparision operators
a
10
b
5
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
#assignmentr operations
a=10
b=5
a+=10
a
20
a-=5
a
15
a*=2
a
30
a//=2
a
15
a/=2
a
7.5
a//=2
a
3.0
a**=2
a
9.0
c=9
c **=2
c
81
c%=2
c
1
#relational operators
a=True
b=False
a and b
False\
a or b
True
'a' in 'aeiou'
True
'd' in 'aeiou'
False
3%2=0
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
3%2==0
False
not 3%2==0
True
#membership operators
s='python programming'
'python' in s
True
'java' in s
False
'a ' in s
False
'a' in s
True
'program' not in s
False
'pras' not in s
True
l=[1,2,3,5]
3 in l
True
9 in l
False
3 not in l
False
t=(1,2,3,9)
1 in t
True
8 in t
False
2 not in t
False
6 not in t
True
s={'p','q','r'}
'p' in s
True
'h' in s
False
'h' not in s
True
d={'name':'prasanna','batch':65,'course':'pfs'}
'prasanna' in d
False
'name' in d
True
'batch' not in d
False
65 not in d
True
>>> #identical operators
>>> ]l=[1,2,3]
>>> l=[1,2,3]
>>> m=[1,2,3]
>>> id(l)
1908157610048
>>> id(m)
1908157516224
>>> l==m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3]
>>> id(n)
1908157516224
>>> n is m
True
>>> m is n
True
>>> n is l
False
>>> n is not l
True
>>> #bitwisw
>>> 11&12
8
>>> 11|12
15
>>> 11^qr
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    11^qr
NameError: name 'qr' is not defined
>>> 11^12
7
>>> ~11
-12
>>> ~-90
89
\
>>> 12<<2
48
>>> 12>>2
3
