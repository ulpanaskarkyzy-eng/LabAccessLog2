from hours_array import HoursArray
from hour_counter import HourCounter
from day_filter import DayFilter

t9 = HoursArray("lab_log.csv")
print("HoursArray:", t9.get_hours())

t10 = HourCounter("lab_log.csv")
print("HourCounter:", t10.count_by_hour())

t11 = DayFilter("lab_log.csv")
print("DayFilter:")
print(t11.get_day("2024-03-15"))