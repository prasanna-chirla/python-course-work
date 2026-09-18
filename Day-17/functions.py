'''
#basic structure (func)

def functionname(arg):
    #stmt
    return()---------optional
functionname(parameters)

def gst(price):
    print("original price: ",price)
    print("final price: ",price*price+0.18)
gst(900)
gst(1000)
gst(8000)

#tables
def table(n):
    print(f"{n}-Table")
    print('----------------')
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
for i in range(1,21):
    table(i)
  
#leap year
def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "leap year"
    else:
        return "not leap year"
print(isleap(2020))
print(isleap(2026))
  
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "not prime"
    return "prime"
print(isprime(23))

#Arguments
#positional arguments
def display(name,mail,pwd):
    print("name:",name)
    print("mail:",mail)
    print("password:",pwd)
display('sam','sam@36','sam1234')
display('sam1234','sam','sam@36')
display('sam@36','sam@36','sam')

#keyword arguments

def display(name,mail,pwd):
    print("name:",name)
    print("mail:",mail)
    print("password:",pwd)
display(name='sam',mail='sam@36',pwd='sam1234')
display(pwd='sam1234',name='sam',mail='sam@36')
display(pwd='sam@36',mail='sam@36',name='sam')

#default arguments
def display(name,mail,pwd=None):
    print("name:",name)
    print("mail:",mail)
    print("password:",pwd)
display('sam','sam@36')
display('sam','sam@36','sam1234')

#variable length arguments
#*-tuple
def display(*names):
    print(names)
display('prasanna')
display('prasanna','sai')
display('prasanna','sai','datta')

#**-dictionary
def display(**names):
    print(names)
display(n1='prasanna')
display(n1='prasanna',n2='datta')
'''



