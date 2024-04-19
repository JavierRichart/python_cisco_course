import calendar

"""calendar.setfirstweekday(calendar.MONDAY)
calendar.prmonth(2024, 3)"""

print(calendar.weekday(2024, 4, 28))
print(calendar.weekheader(2))

print(calendar.isleap(2024))
print(calendar.leapdays(2010, 2025))

"""cal = calendar.Calendar(calendar.SUNDAY)

for weekday in cal.iterweekdays():
    print(weekday, end=" ")"""

"""cal2 = calendar.Calendar()

for iter in cal2.itermonthdays(2024, 11):
    print(iter, end=" ")
"""

"""cal = calendar.Calendar()

for data in cal.monthdays2calendar(2024, 11):
    print(data)"""


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days


my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

print(number_of_days)

print(calendar.weekheader(2))

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")
