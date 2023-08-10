#some module exercises

import random #this is a module

random.randint(1, 10) #this is a function from the module





import datetime #this is a module

now = datetime.datetime.now() # use the now() attribute on the datetime class in the datetime module

print(now) #print the time

now.year #get the year from the datetime object

td = now +  datetime.timedelta(days=28) #timedelta is a duration expressing the difference between two dates.

print(td) #print the new day