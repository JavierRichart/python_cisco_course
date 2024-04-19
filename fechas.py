from datetime import date, datetime, timedelta
import time

"""today = date.today()

print("Hoy", today)
print("Año", today.year)
print("Mes", today.month)
print("Día", today.day)"""

"""timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha", d)

week_day = date(2024, 3, 26)
print(week_day.weekday())
print(week_day.isoweekday())

"""

print(time.ctime())

hoy = date(2024, 3, 25)
print(hoy.strftime('%d/%m/%Y'))

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

print('*' * 8, 'Operaciones con fechas', '*' * 8)

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

print('*' * 8, 'timedelta', '*' * 8)

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)