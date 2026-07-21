import pandas as pd
import json

df_all = []
try:
    with open("data/athletes.json", "r") as f:
        data = json.load(f)
        for i in data:
            print(i.get("notes", ""))
except Exception as e:
    print(e)
