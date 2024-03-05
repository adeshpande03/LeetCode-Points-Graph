from pandas import read_csv, concat, DataFrame
from get_points import get_points
import os
from datetime import datetime
from create_csv import create_csv
import pytz
from get_session import get_session

def update_csv(filename="data.csv"):
    """Updates a csv file with a new entry if the current points value is diferent than the previous one

    Args:
        filename (str, optional): _description_. Defaults to "data.csv".

    Returns:
        new_entry: newest entry to csv
    """
    if not os.path.exists("data.csv"):
        create_csv(filename)
    points = get_points()
    df = read_csv(filename)
    df.drop(df.filter(regex="Unname"), axis=1, inplace=True)
    last_entry = -1
    if len(df) >= 1:
        last_entry = dict(df.iloc[-1])
    new_entry = {
        "datetime": str(datetime.now(pytz.timezone("US/Pacific")).date()),
        "points": points,
    }
    if (
        new_entry["datetime"] == last_entry["datetime"]
        and new_entry["points"] != last_entry["points"]
    ):
        df = df[:-1]
        df = concat([df, DataFrame([new_entry])], ignore_index=True)

    elif new_entry != last_entry:
        df = concat([df, DataFrame([new_entry])], ignore_index=True)

    df.to_csv(filename, index=False)
    return new_entry


if __name__ == "__main__":
    df = update_csv()
    print(df)
