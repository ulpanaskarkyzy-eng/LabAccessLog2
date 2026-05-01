import pandas as pd
import matplotlib.pyplot as plt


class HourPlotter:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_day(self, date_str):
        df = pd.read_csv(self.filepath)
        df["hour"] = df["ts"].apply(lambda ts: int(ts[11:13]))
        df = df[["ts", "hour", "student_id"]]
        return df[df["ts"].str.startswith(date_str)]

    def plot(self, date_str):
        day_df = self.get_day(date_str)
        table = day_df.groupby("hour").size().reset_index(name="entries")

        plt.figure(figsize=(10, 5))
        plt.bar(table["hour"], table["entries"], color="steelblue")
        plt.xlabel("Час дня")
        plt.ylabel("Число входов")
        plt.title(f"Входы в лабораторию за {date_str}")
        plt.xticks(range(0, 24))
        plt.tight_layout()
        plt.savefig("entries_by_hour.png")
        plt.show()
        print("HourPlotter: график сохранён entries_by_hour.png")


obj = HourPlotter("Lab_log.csv")
obj.plot("2026-03-15")
