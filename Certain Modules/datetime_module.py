# datetime module
import datetime

# Python has the datetime module to help deal with timestamps in your code. 
# Time values are represented with the time class. Times have attributes for hour, minute, second, and microsecond. 
# They can also include time zone information. The arguments to initialize a time instance are optional, but the default of 0 is unlikely to be what you want.



#Time

# Let's take a look at how we can extract time informatiion from the datetime module.
# We can create a timestamp by specifying datetime.time(hour, minute, second, microsecond)
t = datetime.time(12, 25, 50, 5555)

# Let's show the difference components
print(t)
print('Hour  :', t.hour)
print('Minute:', t.minute)
print('Second:', t.second)
print('Microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

# Note: A time instance only holds value of time, and not a date associated with the time.

# We can also check the min and max values a time of day can have in the module:
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)

# The min and max class attributes reflect the valid range of times in a single day.
print("\n")


# Dates

# datetime (as you might suspect) also allows us to work with date timestamps. 
# Calendar date values are represented with the date class. 
# Instances have attributes for year, month, and day. It is easy to create a date representing today’s date using the today() class method.

# Let's see some examples:
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

# As with time, the range of date values supported can be determined using the min and max attributes.
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)
print("\n")

# Another way to create new date instances uses the replace() method of an existing date. For example, you can change the year, leaving the day and month alone.
d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)
print("\n")



# Arithmetic
# We can perform arithmetic on date objects to check for time differences. For example:
print(d1)
print(d1)
print(d1-d2)

# This gives us the difference in days between the two dates. You can use the timedelta method to specify various units of times (days, minutes, hours, etc.)
print((d1 - 25 * datetime.timedelta(days = 365)))