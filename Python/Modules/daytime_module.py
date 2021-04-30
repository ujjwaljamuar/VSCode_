import datetime
mytime=datetime.time(2,20,20,200)
print(mytime.minute)
print(mytime)


print('\n')
# print today's date
today=datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

# to print time and date
print(today.ctime())

from datetime import datetime
mydatetime=datetime(2021,3,17,14,20,1)
print(mydatetime)

# date
from datetime import date
date1=date(2021,11,3)
date2=date(2020,11,3)
result=date1-date2
print(result.days)

datetime1=datetime(2020,11,3,22,0)
datetime2=datetime(2020,11,3,12,0)
result1=datetime1-datetime2
print(result1)
print(result1.seconds)