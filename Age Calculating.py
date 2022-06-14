from email.utils import localtime
import time
from calendar import month
import calendar
from datetime import date 

def month_days(month,LeapYear):
    if month in[1,3,5,7,8,10,12]:
        return 31
    elif month in[2,4,6,9,11]:
        return 30
    elif month==2 and LeapYear:
        return 29
    elif month==2 and not LeapYear:
        return 28

def isLeapYears(year):
    def isLeap(year):
        if year%4==0 and year%100 !=0 or year % 400 == 0:
            return True
        else:
            return False

localtime = time.localtime(time.time())
name=input("Enter your name : ")
Birth_Year = int(input("Enter your birth year: "))
Current_year = date.today().year
Age = (Current_year - Birth_Year)
month=Age*12+localtime.tm_mon
begain_year=int(localtime.tm_year)-Age
end_year=begain_year+Age
day=0
for y in range(begain_year,end_year):
    if(isLeapYears(y)):
        day=day+366
    else:
        day=day+365
day=day+localtime.tm_mday
leap_year = isLeapYears(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)
print("%s's age is %d years or " % (name, Age), end="")
print("%d months or %d days" % (month, day))