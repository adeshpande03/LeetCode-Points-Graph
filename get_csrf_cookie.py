from requests import get


def get_csrf_cookie(session_id: str) -> str:
    response = get(
        "https://leetcode.com/",
        cookies={
            "LEETCODE_SESSION": session_id,
        },
    )

    return response.cookies["csrftoken"]
