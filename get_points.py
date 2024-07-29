from requests import Session
import os
import smtplib
from pprint import pprint
def get_points():
    s = Session()
    response = s.get("https://leetcode-api-faisalshohag.vercel.app/impgriffin").json()
    # pprint(response)
    points = response["contributionPoint"]
    # print(points)
    return points

if __name__ == "__main__":
    points = get_points()
    print(points)
