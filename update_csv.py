from pandas import read_csv, concat, DataFrame
from get_points import get_points
import os
from datetime import datetime
from create_csv import create_csv


def update_csv(filename="data.csv"):
    """Updates a csv file with a new entry if the current points value is diferent than the previous one

    Args:
        filename (str, optional): _description_. Defaults to "data.csv".

    Returns:
        df: updated dataframe
    """
    if not os.path.exists("data.csv"):
        create_csv(filename)
    points = get_points()
    df = read_csv(filename)
    df.drop(df.filter(regex="Unname"), axis=1, inplace=True)
    new_entry = {
        "datetime": datetime.now().date(),
        "points": points,
    }
    df = concat([df, DataFrame([new_entry])], ignore_index=True)
    df.to_csv(filename, index=False)
    return df


if __name__ == "__main__":
    df = update_csv()
    print(df)
