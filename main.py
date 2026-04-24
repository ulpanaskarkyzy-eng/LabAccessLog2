from task9 import LabAccessLog2 as Task9
from task10 import LabAccessLog2 as Task10
from task11 import LabAccessLog2 as Task11


t9 = Task9("lab_log.csv")
print("Задание 9:", t9.get_hours())


t10 = Task10("lab_log.csv")
print("Задание 10:", t10.count_by_hour())


t11 = Task11("lab_log.csv")
print("Задание 11:")
print(t11.get_day("2024-03-15"))