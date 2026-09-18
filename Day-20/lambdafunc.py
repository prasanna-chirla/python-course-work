'''
var=lambda arg:exp
'''
#display sentense
wish=lambda name:f"Welcome to course {name}"
print(wish('prasanna'))
print(wish('ramya'))
#gst
gst=lambda price:price+price*0.18
print(gst(1300))
print(gst(1500))
#average
avg=lambda a,b,c:(a+b+c/3)
print(avg(1,2,3))
print(avg(11,21,34))
#even or odd
iseven=lambda a:"even" if a%2==0 else "odd"
print(iseven(23))
print(iseven(98))
#larget number
largest=lambda a,b,c:a if a>b and a>c else (b if b>c else c)
print(largest(23,64,11))
print(largest(3,64,10))
#check vowel or not
isvowel=lambda a:"vowel" if a in 'aeiouAEIOU' else "cons"
print(isvowel('u'))
print(isvowel('g'))
#multiply every element with 10
l=[1,2,3,4,5,6]
update=list(map(lambda i: i+10,l))
print(update)
#update every value with 30% discount
t=(1,2,3,4,5,6)
discount=list(map(lambda i: i-i*0.3,t))
print(tuple(discount))
#filter
#only print odd numbers
l=[1,2,3,4,5,6]
update=list(filter(lambda i: i%2!=0,l))
print(update)

t=(1,2,3,4,5,6000)
update=list(filter(lambda i: i>1000,t))
print(update)
#print  only domain names
l=['prasanna@gmail.com','prasanna@yahoo.com','prasanna@codegnan.com']
res=list(map(lambda i:i.split('@')[-1],l))
print(res)
#reduce-large nums into single unit
from functools import reduce
l=[2,5,3,7,2,7,21,54]
res1=reduce(lambda sum,i:sum+i,l)
print(res1)

from functools import reduce
l=[2,5,3,7,2,7,21,54]
res1=reduce(lambda p,i:p*i,l)
print(res1)
#print available seats
seats={'s1':True,
          's2':False,
          's3':False,
          's4':False,
          's5':True,
          's6':True}
available=list(filter(lambda i:seats[i]!=True,seats))
print(available)
#
products={
    'eggs':80,
    'sugar':180,
    'curd':30,
    'salt':18}
res=list(filter(lambda i:products[i]>50,products))
print(res)
#
products={
    'eggs':80,
    'sugar':180,
    'curd':30,
    'salt':18}
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))




