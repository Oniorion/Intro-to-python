# Question 1
import sys
for line in sys.stdin:
    data = line.strip().split("t")
    if len (data) == 6:
        # Made (date =) so line 3 can complete
        data = date,time,store,item,cost,payment = data
        # Added ()
        print ('{0}\t{1}'.format(item, cost))

# Question 2
# Part of the python daytime libary
# Used to calculate differences in dates
from datetime import timedelta
from datetime import datetime
# We subtract 60 seconds
print (datetime.now () - timedelta (seconds = 60))
# We add 2 years
print (datetime.now () + timedelta (days = 720))
# We add a Day
print (datetime.now () + timedelta (days = 1))

# Question 3
from datetime import datetime
from datetime import timedelta
d = timedelta (microseconds = -1)
print (d.days, d.seconds, d.microseconds)
# 100 days, 10 hours, 13 min. = 144613
e = timedelta (minutes = 144613)
print (e.days, e.seconds)

# Question 4
from datetime import datetime

datetime_object = datetime.now ()
# Defines user input for feet and inches
def Measurement (f, i, z):
    print ("Feet",f)
    print ("Inches",i)
    print (z)
# Takes user input for f feet and i inches
f = input ("Enter in feet ")
i = input ("Enter in inches ")
Measurement (f,i,datetime_object)
