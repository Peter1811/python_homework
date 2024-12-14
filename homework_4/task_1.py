import datetime
import time

# текущая дата
current_date = datetime.datetime.now()
print(current_date)
print()

# разница между двумя датами
current_date_1 = datetime.datetime.now()
current_date_2 = datetime.datetime(year=2024, 
                                   month=12, 
                                   day=14, 
                                   hour=13, 
                                   minute=18, 
                                   second=59)

print(current_date_2 - current_date_1)
print()

# преобразование строки в объект даты и времени.
str_to_dt = '2007-12-02 12:30:45'
res_dt = datetime.datetime.strptime(str_to_dt, '%Y-%m-%d %H:%M:%S')
print(res_dt)
print(type(res_dt))
