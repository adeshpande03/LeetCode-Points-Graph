from pandas import DataFrame


def create_csv(filename="data.csv"):
    df = DataFrame(columns=["datetime", "points"])
    df.to_csv(filename)
    return


if __name__ == "__main__":
    create_csv()
