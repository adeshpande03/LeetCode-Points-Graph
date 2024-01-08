from requests import Session
import os


def get_points(LEETCODE_SESSION=os.environ.get("LEETCODE_SESSION")):
    BASE_URL = "https://leetcode.com/"
    POINTS_URL = BASE_URL + "points/api/total"
    if not os.environ.get("LEETCODE_SESSION"):
        raise RuntimeError("LEETCODE_SESSION not set")
    cookies = {"LEETCODE_SESSION": LEETCODE_SESSION}
    s = Session()
    s = s.get(
        POINTS_URL,
        cookies=cookies,
    )
    status_code = s.status_code
    status_set = {200}
    if status_code not in status_set:
        raise RuntimeError(
            f"Status code: {status_code} is invalid. Check LEETCODE_SESSION or manually set csrf to troubleshoot."
        )
    return s.json()["points"]


if __name__ == "__main__":
    points = get_points()
    print(points)
