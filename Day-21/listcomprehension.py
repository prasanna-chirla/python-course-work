#list
'''l=[]
for i in range(1,11):
    l.append(i)
print(l)
|
|
|
>

#print 1 to 10
l=[i for i in range(1,11)]
print(l)
#factors
n=12
f=[i for i in range(1,n+1) if n%i==0]
print(f)
#even and odd places
x=[1,2,3,4,5,6]
y=[i if i%2==0 else 0 for i in x]
print(y)

#even positions
m=[i for i in range(2,11,2)]
print(m)

l=[[j for j in range(1,4)] for i in range(3)]
print(l)                       ----------------------->
l = []

l=[]
for i in range(3):
    row = []
    for j in range(1, 4):
        row.append(j)
    l.append(row)
print(l)
'''
#set comprehension
s={i for i in range(1,11)}
print(s)
#dictionary comprehension
s={i:i*i for i in range(1,11)}
print(s)






