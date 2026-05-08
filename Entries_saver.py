import pandas as pd


class EntriesSaver:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_day(self, date_str):
        df = pd.read_csv(self.filepath)
        df["hour"] = df["ts"].apply(lambda ts: int(ts[11:13]))
        return df[df["ts"].str.startswith(date_str)]

    def save_by_hour(self, date_str):
        day_df = self.get_day(date_str)
        table = day_df.groupby("hour").size().reset_index(name="entries")
        table.to_csv("entries_by_hour.csv", index=False)
        print("EntriesSaver: сохранено в entries_by_hour.csv")
        print(table)
        return table


obj = EntriesSaver("Lab_log.csv")
obj.save_by_hour("2026-03-15")
