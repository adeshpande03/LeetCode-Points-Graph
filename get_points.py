from requests import Session
import os
import smtplib


def get_points(LEETCODE_SESSION=os.environ.get("LEETCODE_SESSION")):
    print(LEETCODE_SESSION)
    BASE_URL = "https://leetcode.com/"
    POINTS_URL = BASE_URL + "points/api/total"
    cookies = {"LEETCODE_SESSION": LEETCODE_SESSION}
    s = Session()
    s = s.get(
        POINTS_URL,
        cookies=cookies,
    )
    status_code = s.status_code
    status_set = {200}
    if status_code not in status_set:
        CARRIERS = {
            "tmobile": "@tmomail.net",
            "verizon": "@vtext.com",
        }
        EMAIL = os.environ.get("EMAIL")
        APP_PASSWORD = os.environ.get("APP_PASSWORD")
        PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

        def send_message(
            carrier,
            message,
            PHONE_NUMBER=PHONE_NUMBER,
        ):
            recipient = PHONE_NUMBER + CARRIERS[carrier]
            auth = (EMAIL, APP_PASSWORD)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(auth[0], auth[1])
            server.sendmail(auth[0], recipient, message)

        message = "Please fix Leetcode Points graph, your LEETCODE_SESSION is invalid"
        send_message("verizon", message)

        raise RuntimeError(
            f"Status code: {status_code} is invalid. Check LEETCODE_SESSION or manually set csrf to troubleshoot."
        )

    return s.json()["points"]


if __name__ == "__main__":
    points = get_points()
    print(points)
