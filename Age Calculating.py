from email.utils import localtime
import time
import calendar
from calendar import isleap, month

def isLeap(year):
    if year%4==0 and year%100 !=0 or year % 400 == 0:
        return True
    else:
        return False
def month_days(month,leap_year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in[2,4,6,9,11]:
        return 30
    elif month == 2 and leap_year:
        return 29

    elif month==2 and (not leap_year):
        return 28

name=input("Enter Your Name : ")
year=int(input("Enter Year : "))
localtime = time.localtime(time.time())


month = year * 12 + localtime.tm_mon

begain_year=int(localtime.tm_year)- year
end_year= begain_year+year
day=0

for y in range(begain_year,end_year):
    if (isLeap(y)):
        day= day + 366
    else:
        day = day + 365

day=day+localtime.tm_mday

leap_year = isLeap(localtime.tm_year)

for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
