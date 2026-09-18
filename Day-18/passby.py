#int float complex str list tuple set dict bool

#list dict set-immutable
#pass by value-Pass by value: A copy of the value is passed to the function, so changes inside the function do not affect the original variable.
#int
'''
def display(n):
    n+=10
    print("inside function: ",n)
n=20
display(n)
print("outside function: ",n)
#float
def display(n):
    n+=10.3
    print("inside function: ",n)
n=20
display(n)
print("outside function: ",n)
#complex

def display(n):
    n=10+40j
    print("inside function: ",n)
n=20
display(n)
print("outside function: ",n)

#string
def display(n):
    n+='prog'
    print("inside function: ",n)
n='lang'
display(n)
print("outside function: ",n)

#pass by reference-Pass by reference: A reference to the original variable is passed, so changes inside the function can affect the original variable.
#list
def display(n):
    n.append[3]
    print("inside function: ",n)
n=[5,6]
display(n)
print("outside function: ",n)

#set
def display(n):
    n.add(1)
    print("inside function: ",n)
n={5,6}
display(n)
print("outside function: ",n)

#tuple
def display(n):
    n.add(1)
    print("inside function: ",n)
n={5,6}
display(n)
print("outside function: ",n)

#dictionary
def display(n):
    n[5]=6
    print("inside function: ",n)
n={1:2,3:4}
display(n)
print("outside function: ",n)
'''
def display(n):
    n.add(1)
    print("inside function: ",n)
n={5,6}
display(n)
print("outside function: ",n)