import pandas as pd
import numpy as np


class HourCounter:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_hours(self):
        df = pd.read_csv(self.filepath)
        hours = []
        for ts in df["ts"]:
            hours.append(int(ts[11:13]))
        return np.array(hours)

    # считаем сколько входов в каждом из 24 часов
    def count_by_hour(self):
        hours = self.get_hours()
        counts = np.bincount(hours, minlength=24)
        return counts


obj = HourCounter("Lab_log.csv")
print("HourCounter:", obj.count_by_hour())
