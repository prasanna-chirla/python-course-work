#print(n) after display(n+1) prints the numbers during the recursion’s return (backtracking)
#  so they appear in reverse order.
#print 10 t0 1
'''
def display(n):
    if n==11:
        return 
    display(n+1)
    print(n)
display(1)

#string reverse
def display(s, i):
    if i == len(s):    
        return
    display(s, i + 1)
    print(s[i],end='')
s = input("Enter: ")
display(s, 0)

def display(s,i,w):
    if len(s)-w+1==i:
        return
    print(s[i:i+w])
    display(s,i+1,w)
s=input()
w=int(input())
display(s,0,w)
output:
prasanna
4
pras
rasa
asan
sann
anna

#summation of list elements
def display(l,i):
    if i==len(l):
        return 0
    return l[i] + display(l,i+1)
l=[43,23,54,22]
print(display(l,0))

#sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

n = int(input())
print(sum_digits(n))

#factorial
def display(n):
    if n==1:
        return 1
    return n*display(n-1)
n=int(input())
print(display(n))

#fibonacci
n=int(input("enter: "))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=' ')
        '''

#fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter: "))
for i in range(n):
    print(fibonacci(i),, end=" ")
       
    
