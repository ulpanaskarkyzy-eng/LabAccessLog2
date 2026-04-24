import pandas as pd


class DayFilter:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_day(self, date_str):
        df = pd.read_csv(self.filepath)

        df["hour"] = df["ts"].apply(lambda ts: int(ts[11:13]))

        df = df[["ts", "hour", "student_id"]]

        day_df = df[df["ts"].str.startswith(date_str)]
        return day_df


obj = DayFilter("lab_log.csv")
print("DayFilter:")
print(obj.get_day("2024-03-15"))
