import pandas as pd
import numpy as np


class LabAccessLog2:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_hours(self):
        df = pd.read_csv(self.filepath)
        hours = []
        for ts in df["ts"]:
            hour = int(ts[11:13])
            hours.append(hour)
        return np.array(hours)


obj = LabAccessLog2("lab_log.csv")
hours = obj.get_hours()
print("Массив часов:", hours)
