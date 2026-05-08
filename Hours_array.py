import pandas as pd
import numpy as np


class HoursArray:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_hours(self):
        df = pd.read_csv(self.filepath)
        hours = []
        for ts in df["ts"]:
            hour = int(ts[11:13])
            hours.append(hour)
        return np.array(hours)


obj = HoursArray("Lab_log.csv")
print("HoursArray:", obj.get_hours())