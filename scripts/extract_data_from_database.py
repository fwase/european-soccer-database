import os
import sqlite3
import sys

import pandas as pd

tables = [
    "country",
    "league",
    "match",
    "player",
    "player_attributes",
    "team",
    "team_attributes",
]


def main(sqlite_file, folder_output):
    connector = sqlite3.connect(sqlite_file)

    os.makedirs(folder_output, exist_ok=True) 

    for table in tables:
        data_df = pd.read_sql_query(f"SELECT * FROM {table}", connector)

        file_name = os.path.join(folder_output, f"{table}.csv")
        data_df.to_csv(file_name, index=False)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
