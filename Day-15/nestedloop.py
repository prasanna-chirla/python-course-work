                                                                                                                            
'''for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()
output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

for i in range(5):
    for j in range(5):
        print(j%2,end=' ')
    print()
output:
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 


for i in range(5):
    for j in range(5):
        print(i%2,end=' ')
    print()
output:
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 


for i in range(5):
    for j in range(5):
        print((i+j)%2,end=' ')
    print()
output:
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0

for i in range(5):
    for j in range(5):
        print((i+j),end=' ')
    print() 
output:
0 1 2 3 4 
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 


count=1
for i in range(5):
    for j in range(5):
        print(count,end=' ')
        count+=1
    print()
output:
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 


#level 2
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()
output:
* 
* * 
* * * 
* * * * 
* * * * * 


for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()
output:
* * * * * 
* * * * 
* * * 
* * 
*


for i in range(5):
    for j in range(5-i-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()
output:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 


n=int(input("enter"))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print()
output:
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 

n=int(input("enter: "))
m=n//2
for i in range(n):
    if i <=m:
    for j in range(i+1):
        
        print('*',end=' ')
    else:
        for k in range(n-i):
            print('* ',end=' ')

    print()

|
|
|
#optimized
n=int(input("enter: "))
m=n//2
for i in range(n):
    if i <=m:
        print('* '*(i+1),end=' ')
    else:
              print('* '*(n-i),end=' ')
    

    print()
output:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

n=int(input("enter: "))
m=n//2
for i in range(n):
    if i <=m:
        print(' '*(m-i),'*'*(i+1),end=' ')
    else:
              print(' '*(i-m),'*'*(n-i),end=' ')
    

    print()
output:
enter: 9
     * 
    ** 
   *** 
  **** 
 ***** 
  **** 
   *** 
    ** 
     * 

#just add spaces to above program
n=int(input("enter: "))
m=n//2
for i in range(n):
    if i <=m:
        print(' '*(m-i),'* '*(i+1),end=' ')
    else:
              print(' '*(i-m),'* '*(n-i),end=' ')
    

    print()
output:
enter: 9
     *  
    * *  
   * * *  
  * * * *  
 * * * * *  
  * * * *  
   * * *  
    * *  
     *  
'''





