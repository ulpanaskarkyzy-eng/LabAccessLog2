import pandas as pd
from flask import Flask, jsonify, request


class LabApi:
    def __init__(self, filepath):
        self.filepath = filepath
        self.app = Flask(__name__)
        self.app.add_url_rule("/entries", "entries", self.entries)

    def get_day(self, date_str):
        df = pd.read_csv(self.filepath)
        df["hour"] = df["ts"].apply(lambda ts: int(ts[11:13]))
        df = df[["ts", "hour", "student_id"]]
        return df[df["ts"].str.startswith(date_str)]

    def entries(self):
        date_str = request.args.get("date", "")
        if not date_str:
            return jsonify({"error": "укажите параметр ?date=ГГГГ-ММ-ДД"}), 400
        day_df = self.get_day(date_str)
        table = day_df.groupby("hour").size().reset_index(name="entries")
        return jsonify(table.to_dict(orient="records"))

    def run(self):
        self.app.run(debug=True)


obj = LabApi("Lab_log.csv")
obj.run()
