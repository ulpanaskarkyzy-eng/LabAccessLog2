from Hours_array import HoursArray
from Hour_counter import HourCounter
from Day_filter import DayFilter
from Entries_saver import EntriesSaver
from Hour_plotter import HourPlotter

t9 = HoursArray("Lab_log.csv")
print("HoursArray:", t9.get_hours())

t10 = HourCounter("Lab_log.csv")
print("HourCounter:", t10.count_by_hour())

t11 = DayFilter("Lab_log.csv")
print("DayFilter:")
print(t11.get_day("2024-03-15"))

t12 = EntriesSaver("Lab_log.csv")
t12.save_by_hour("2024-03-15")

t13 = HourPlotter("Lab_log.csv")
t13.plot("2024-03-15")