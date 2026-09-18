#system module
'''
import sys
print(sys.argv[-1])  #sys.argv stores command-line arguments as a list.
print(sys.version) 
print(sys.path)
print("start")
sys.exit()
print("end")

#platform module
import platform
print(platform.system())
print(platform.release())
print(platform.processor())

#math module
import math
print(math.pi)  #pi value
print(math.e)    #e value(eulers)
print(math.log(2,2))   #logarithm
print(math.sin(30))   #sin angle
print(math.tan(30))    #tan angle
print(math.cos(30))     #cos angle
print(math.degrees(30))   #convert deg to rad
print(math.radians(30))    #convert rad to deg
print(math.factorial(5))     #factorial
print(math.gcd(8,12))        #greatest common divisor
print(math.pow(2,3))            #power
print(math.sqrt(36))       #square root

print(round(12.00000001))
print(round(12.3))
print(round(12.6666))
print(round(12.999999))
#upper value
print(math.ceil(12.00000001))
print(math.ceil(12.3))
print(math.ceil(12.6666))
print(math.ceil(12.999999))
#lower value
print(math.floor(12.00000001))
print(math.floor(12.3))
print(math.floor(12.6666))
print(math.floor(12.999999))

#random module
# Import the random module
import random
# Set the seed value to 9
#one random output is fixed
random.seed(9)
# Generate a random floating-point number between 0.0 and 1.0
print(random.random())
# Generate a random integer between 10,000 and 999,999 (both included)
print(random.randint(10000, 999999))
# Generate a random floating-point number between 1 and 6
print(random.uniform(1, 6))
# Create a list containing three values
l = ['r', 'p', 's']
# Select one random element from the list
print(random.choice(l))
# Create a list of programming languages
lang = ['python', 'java', 'js', 'c', 'c++']
# Select 2 random elements from the list
# Elements can be repeated because choices() uses replacement
print(random.choices(lang, k=2))
# Randomly rearrange (shuffle) the elements of the list
random.shuffle(lang)
print(lang)

#collections module
#Counter is a Python class from collections that counts how many times each element occurs in a sequence.
from collections import Counter
s='python programming'
res=Counter(s)
print(dict(res))

#defaultdict is a dictionary from the collections module that automatically provides a default value when a key doesn't exist.
from collections import defaultdict
products=['sugar','salt','milk']
res=defaultdict(list)
for i in products:
    res[i].append(['des','rev','com'])
print(res)

from collections import defaultdict
s='python programming'
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
'''
#queue-first in first out
from collections import deque
l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.append(40)
l.popleft()
l.append(45)
l.pop()
l.appendleft(35)
print(l)

#password generatotr
import random
name = input("Enter your name: ").title()
dob = input("Enter your DOB (DDMMYYYY): ")
spc=['@','!','#','%','&']
password = name+random.choice(spc)+dob[-4:]
print("Generated Password:", password)






