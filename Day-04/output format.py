Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=20
>>> c='codegnan'
>>> print(a,b,c)
10 20 codegnan
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 20 c= codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=10b=20c=codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
20
c=
codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	20	c=	codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\n',end='\n\n')
a=
10
b=
20
c=
codegnan

>>> #end used for row space operations and sep for column space operations
>>> print('a=',a,'b=',b,'c=',c,sep='\n',end='@')
a=
10
b=
20
c=
codegnan@
>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='@')
a=	10	b=	20	c=	codegnan@
>>> print(f'a={a} b={b} c={{c}')
SyntaxError: f-string: single '}' is not allowed
>>> print(f'a={a} b={b} c={c}')
a=10 b=20 c=codegnan
>>> a=10 b=20 c=codegnan
SyntaxError: invalid syntax
>>> print('a=%d b=%f c=%s',(a,b,c))
a=%d b=%f c=%s (10, 20, 'codegnan')
print(f'a={a} b={b} c={c}'.format(a,b,c))
a=10 b=20 c=codegnan
print(f'a={3} b={0} c={1}'.format(a,b,c))
a=3 b=0 c=1
print(f'a={2} b={0} c={1}'.format(b,a,c))
a=2 b=0 c=1
a=10
b=20
c='codegnan'
SyntaxError: multiple statements found while compiling a single statement
a=90
b=40
c='coodegnan'
SyntaxError: multiple statements found while compiling a single statement
