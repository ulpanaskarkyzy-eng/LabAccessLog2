from Hours_array import HoursArray
from Hour_counter import HourCounter
from Day_filter import DayFilter

t9 = HoursArray("Lab_log.csv")
print("HoursArray:", t9.get_hours())

t10 = HourCounter("Lab_log.csv")
print("HourCounter:", t10.count_by_hour())

t11 = DayFilter("Lab_log.csv")
print("DayFilter:")
print(t11.get_day("2024-03-15"))