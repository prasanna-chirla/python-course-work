'''from datetime import date,time,datetime,timedelta
t=date.today()
print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())#0 to 6 days

year,month,day=list(map(int,input('[yyyy-mm-dd]').split('-')))
print(date(year,month,day))

#time
tm=time(23,6,6)
print(tm)
print(tm.minute)#0 t0 59
print(tm.hour)#0 to 23
print(tm.second)#0 to 59

#datetime
from datetime import datetime
dt= datetime.now()
print(dt)#2026-09-05 17:44:17.019789
print(dt.strftime('%d-%m-%y'))#05-09-26(y)
print(dt.strftime('%d-%m-%Y'))#05-09-2026(Y)
print(dt.strftime('%d-%m-%Y %H:%M:%S'))#05-09-2026 17:44:17(H)
print(dt.strftime('%d-%m-%Y %I:%M:%S'))#05-09-2026 05:44:17(I)
print(dt.strftime('%d-%m-%Y %H:%M:%S %p'))#05-09-2026 17:44:17 PM(p)
print(dt.strftime('%d-%b-%Y %H:%M:%S'))#05-Sep-2026 17:44:17(b)
print(dt.strftime('%d-%B-%Y %H:%M:%S'))#05-September-2026 17:44:17(B)
print(dt.strftime('%a,%d-%m-%Y %H:%M:%S'))#Sat,05-09-2026 17:44:17(a)
print(dt.strftime('%A,%d-%m-%Y %H:%M:%S'))#Saturday,05-09-2026 17:44:17(A)

#timedelta(add time and date and check before or previous)
from datetime import date,time,datetime,timedelta
dt=datetime.now()
t=date.today()
t7=t+timedelta(days=7)
tp=t-timedelta(days=7)
m15=dt+timedelta(minutes=15)
print(t7,tp,m15)
'''
from itertools import permutations,combinations
s='abc'
res1=list(permutations(s,2))
print([''.join(i) for i in res1])
res2=(list(combinations(s,2)))
print([''.join(i) for i in res2])
