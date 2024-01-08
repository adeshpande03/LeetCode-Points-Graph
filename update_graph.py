from get_points import get_points
from create_csv import create_csv
import os


def main():
    LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
    if not os.path.exists("data.csv"):
        create_csv()


if __name__ == "__main__":
    main()
