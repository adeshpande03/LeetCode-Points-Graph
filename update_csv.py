from pandas import read_csv, concat, DataFrame
from get_points import get_points
import os
from datetime import datetime


def update_csv(filename="data.csv"):
    """Updates a csv file with a new entry if the current points value is diferent than the previous one

    Args:
        filename (str, optional): _description_. Defaults to "data.csv".

    Returns:
        df: updated dataframe
    """
    points = get_points()
    df = read_csv(filename)
    df.drop(df.filter(regex="Unname"), axis=1, inplace=True)
    last_points_entry = -1
    if len(df) >= 1:
        last_points_entry = dict(df.iloc[-1])["points"]

    new_entry = {
        "entry_no.": len(df) + 1,
        "datetime": datetime.now().date(),
        "points": points,
    }
    df = concat([df, DataFrame([new_entry])], ignore_index=True)
    df.to_csv(filename, index=False)
    return df


if __name__ == "__main__":
    df = update_csv()
    print(df)
