#Python time
"""""""""
The time module works as unix epoch time, The Unix epoch start time is 
00:00:00 UTC on 1 January 1970`
It is the number of seconds elapsed from the Unix epoch start time.
"""""""""
import time

epoch_secs = time.time()
print(epoch_secs)
curr_local_time = time.ctime()
print(curr_local_time)

"""""""""
* Here we demonstrate extracting parts of the date and time
* Convert date and time to string
* The following is the character to use with `strftime` to convert date to string
"""""""""

import time

# Convert Time to String in desired format
x = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(x)

# Extract Year, Month, Month Name, Day Of Week, Day Name
Year = time.strftime("%Y", time.localtime())
Month = time.strftime("%B", time.localtime())
MonthName = time.strftime("%B", time.localtime())
DayOfWeek = time.strftime("%w", time.localtime())
DayName = time.strftime("%a", time.localtime())

print(Year)
print(Month)
print(MonthName)
print(DayOfWeek)
print(DayName)

"""""
`time.sleep()` is a function that can be used to pause the code execution 
for the specified number of seconds.
"""""

# Here we pause the code execution for 5 Seconds
print(time.ctime(),'Before Sleep')
time.sleep(5)
print(time.ctime(),'After Sleep')




