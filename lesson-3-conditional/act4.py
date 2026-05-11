import calendar
import datetime

current_time = datetime.datetime.now()

print("The time at Greenwich Meridian now is:", end = " ")
print(current_time)

year = int(input("Enter the year: "))
print("\n",calendar.calendar(year))