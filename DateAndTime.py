#Collection of Challenges in Domain Python->Date and Time of Hackerrank

#https://www.hackerrank.com/challenges/calendar-module
import calendar
date=input().split()
year=int(date[2])
month=int(date[0])
day=int(date[1])
weekday=calendar.weekday(year,month,day)
print(calendar.day_name[weekday].upper())

#https://www.hackerrank.com/challenges/python-time-delta
from datetime import datetime
t=int(input())
for i in range(0,t):
    time1=datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z" )
    time2=datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z" )
    diff=(time1-time2).total_seconds()
    print(abs(int(diff)))