import pandas as pd
import numpy as np


class LabAccessLog2:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_hours(self):
        df = pd.read_csv(self.filepath)
        hours = []
        for ts in df["ts"]:
            hours.append(int(ts[11:13]))
        return np.array(hours)

    def count_by_hour(self):
        hours = self.get_hours()
        counts = np.bincount(hours, minlength=24)
        return counts


obj = LabAccessLog2("lab_log.csv")
counts = obj.count_by_hour()
print("Входов по часам (0-23):", counts)
