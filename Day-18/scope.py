'''
#outside function not printed gives error because n scope declares inside function -local variable
def display():
    n=19
    print("inside function: ",n)
display()
print("outside function: ",n)


# n scope can be accessed in both inside and outside function-global variable
def display():
    print("inside function: ",n)
n=19
display()
print("outside function: ",n)


# global used for local variable to access inside and outside of function
def display():
    global n
    n=10
    print("inside function: ",n)
display()
print("outside function: ",n)

#we cant pass n as parameter as n is global
def display():
    global n
    n+=5
    print("inside function: ",n)
n=10
display()
print("outside function: ",n)
output:
inside function:  15
outside function:  15

#global → modifies a variable in the global scope; nonlocal → modifies a variable in the nearest enclosing function scope.
def display():
    course='pfs'
    def update():
        nonlocal course
        course='jfs'
        print("inner function: ",course)
    update()
    print("outer function: ",course)
display()

#This example shows that assigning max = 20 overwrites Python’s built-in max() function, so you can no longer use max() normally.
l=[1,2,3,4,5]
print(max(l))

max=20
print(max)
'''


