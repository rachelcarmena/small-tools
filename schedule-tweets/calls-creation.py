#!/usr/bin/python

from datetime import date
from calendar import monthrange

miliseconds = 0
today = date.today()
day = today.day
month = today.month
year = today.year
days_of_the_month = monthrange(year, month)[1]
for alias in open('Twitter-aliases.txt'):
    miliseconds += 3000
    day += 1
    go_to_next_month = 0
    if day > days_of_the_month:
        day = 1
        go_to_next_month = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
        days_of_the_month = monthrange(year, month)[1]

    print "setTimeout(createTweet, {0}, '{1}', {2}, {3});".format(miliseconds, alias[:-1], day, go_to_next_month)
    
