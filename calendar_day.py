import calendar

date = input('Enter the date (dd/mm/yy): ')
day = int(date.split('/')[0])
month = int(date.split('/')[1])
year = int(date.split('/')[2])

day_index = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_index]
print (date, 'was',day_name)
