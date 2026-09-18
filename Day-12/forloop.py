#if we know how many steps -for loop(ex:insta posts)--------while(ex:snake and ladders we dont know how many moves)
#str list tuple set dict range
#for var in seq:
# stmts
'''
str='programming language'
for i in str:
    print(i)
   
l=[12,34,56,88]
for num in l:
    print(num)
       
prices=(456,897,456,578)
for price in prices:
    print(price)
   

names={'prasanna','priyanka','gayathri'}
for name in names:
    print(name)
   
d={1:2,3:4,5:6,7:8}
for k in d:
    print(k,d[k])
    '''

#range will give numeric values
#range(start,end+1,step):(0,,1)
#1 to 10 nums
'''
for i in range(1,11):
    print(i)
#even nums
for i in range(2,21,2):
    print(i)
#5 multiples
for i  in range(5,101,5):
    print(i)
#5 to 1
for i in range(5,0,-1):
    print(i)
#19 to 1 odd nums
for i in range(19,0,-2):
    print(i)

#if we want val of index also
s='java programming language'
for i in range(len(s)):
    print(i,s[i])
    #can use for list and tuple also
    #dont use for set and dict because no index
   
l=[12,34,56,88]
for num in range(len(l)):
    print(num,l[num])

l=(12,34,56,88)
for num in range(len(l)):
    print(num,l[num])
   
#enumerate
l=[12,34,56,88]
for i in enumerate(l):
    print(i[0],i[1])

l=(12,34,56,88)
for i in enumerate(l):
    print(i[0],i[1])

l={12,34,56,88}
for i in enumerate(l):
    print(i[0],i[1])

d={1:2,3:4,5:6,7:8}
for k in enumerate(d):
    print(k[0],k[1],d[k[1]])

l=(12,34,56,88)
for i in enumerate(l):
    print(i)
      
#break
for i in range(1,11):
    if i==5:
        break
    print(i)
#continue
for i in range(1,11):
    if i==5:
        continue
    print(i)
   
    #for-else:::::
    

for i in range(1,11):
    if i==55:
        break
    print(i)
else:
    print("end of loop")



l=[12,34,56,88]
n=34
for num in l:
    if num==n:
        print(n,"found")
        break
else:
    print(n,"not found")
       

#phone unlock
pin=1234
for i in range(5):
    epin=int(input("enter pin"))
    if epin==pin:
        print("unlock phone")
        break
    else:
        print("invalid pin")
else:
    print("try after 30 seconds")
  '''
#prime number
n=int(input("enter number"))
for i in range(2,n//2+1):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")

    


    
 


