#recursion-a function calling itself and stop when it reach base condition
'''structure:
def fun(arg):
    if base:
        return
    fun(up arg)
fun(para)

#print 1 to 10
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)  

#print 10 to 1
def display(n):
    if n==0:
        return 
    print(n)
    display(n-1)
display(10)

def display(s, i):
    if i == len(s):    
        return

    print(s[i])
    display(s, i + 1)

s = input("Enter: ")
display(s, 0)
'''
