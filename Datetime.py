"""""""""
from datetime import date

# 1. Get the date
today = date.today()
print(today)

# 2. Breakdown Date data
today = date.today()
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

import datetime

l_date_time_string = "2016-06-24"
l_datetime = datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d")
print(l_datetime)

## Python datetime strftime(): Convert DATE and TIME to String
# Use `strftime()` to convert date to string

import datetime

# Convert Date to String
today = datetime.date.today()
# format YYYYMMDD
format1 = "%Y%m%d"
# Print Format
s = today.strftime(format1)
print(s)


# Format DD-MON-YYYY
format2 = "%d-%b-%Y"
# Print Format
s = today.strftime(format2)
print(s)


# Format DD-MON-YYYY HH24:MI:SS
format3 = "%d-%b-%Y %H:%M:%S"
# Print Format
s = today.strftime(format3)
print(s)



import datetime

##################################
# Convert String to Date
##################################
l_date_time_string = "2016-06-24"
l_datetime = datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d")
print(l_datetime)

# Convert String to Date Time in format; DD-MON-YYYY HH24:MI:SS
l_date_string1 = "2016-06-24 16:00:00"
format4        = "%Y-%m-%d %H:%M:%S"
t1 = datetime.datetime.strptime(l_date_string1, format4)
print("t1", t1)

# Get Todays Date Time in format4
s = today.strftime(format4)

# Convert string s back to date time in format4
t2=datetime.datetime.strptime(s, format4).date()


# Comparison
D1_str = "2016-06-24"
D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
print("D1 ",D1)

D2_str = "2016-07-24"
D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
print("D2 ",D2)


if(D1 > D2):
    print(D1," is Greater than ",D2)
else:
    print(D1," is Less than ",D2)


import datetime
from datetime import timedelta

################################################################################
# Subtracting Dates
################################################################################
D1_str = "2016-06-24"
D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
print("D1 ",D1)

D2_str = "2016-07-21"
D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
print("D2 ",D2)

# Difference between TWO Dates in DAYS, Difference in Hours, Minutes and Seconds
diff_in_days = abs(D2 - D1).days
print(diff_in_days)

# Do a Diff between Dates
date_diff = D2 - D1

# Get Diff in Hours using the total_seconds()/3600
diff_in_hours = date_diff.total_seconds() / 3600
print(diff_in_hours)

# Get Diff in Minutes using the total_seconds()/60
diff_in_minutes = date_diff.total_seconds() / 60
print(diff_in_minutes)

# Get Diff in Seconds using the total_seconds()
diff_in_seconds = date_diff.total_seconds() / 60
print(diff_in_seconds)



# Adding to Date - Times
D3_str = '2016-07-21 12:30:22'
formatADT = "%Y-%m-%d %H:%M:%S"

D3 = datetime.datetime.strptime(D3_str, formatADT)
print("D3 DATE-TIME",D3)

# Add 5 Days to D3 using timedelta
######################################
newDate = D3 + timedelta(days=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Days', s)

# Add 5 Hours to D3 using timedelta
######################################
newDate = D3 + timedelta(hours=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Hours', s)

# Add 5 Minutes to D3 using timedelta
######################################
newDate = D3 + timedelta(minutes=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Minutes', s)


# Add 5 Seconds to D3 using timedelta
######################################
newDate = D3 + timedelta(seconds=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Seconds', s)


"""""
#Python Datetime Timezone

import datetime
import pytz
# CREATE DATE AT A TIMEZONE

str_datetime = '2019-05-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# Assign current Date to EST TimeZone
EST_TimeZone = pytz.timezone('America/New_York')
est_date = EST_TimeZone.localize(l_date_time)

print('est_date', est_date)
print('est_date timezone', est_date.tzinfo)



# CONVERT A DATETIME AT A TIMEZONE TO ANOTHER TIMEZONE
str_datetime = '2019-05-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# Assign current Date to EST TimeZone
EST_TimeZone = pytz.timezone('America/New_York')
est_date = EST_TimeZone.localize(l_date_time)

print('est_date', est_date)
print('est_date timezone', est_date.tzinfo)

# Convert EST Date to GMT / UTC using "astimezone"
GMT_TimeZone = pytz.timezone('GMT')
gmt_date = est_date.astimezone(GMT_TimeZone)

print('gmt_date', gmt_date)
print('gmt_date timezone', gmt_date.tzinfo)


# Convert EST Date to INDIA TIMEZONE
IN_TimeZone = pytz.timezone('Asia/Kolkata')
india_date = est_date.astimezone(IN_TimeZone)

print('india_date', india_date)
print('india_date timezone', india_date.tzinfo)

















