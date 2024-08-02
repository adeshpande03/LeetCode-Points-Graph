import requests
import os
import smtplib
from pprint import pprint


def get_points():
    username = "impgriffin"
    url = "https://leetcode.com/graphql"
    headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com"}

    query = """
    query getUserProfile($username: String!) {
        activeDailyCodingChallengeQuestion {
		date
		userStatus
		link
		question {
			acRate
			difficulty
			freqBar
			frontendQuestionId: questionFrontendId
			isFavor
			paidOnly: isPaidOnly
			status
			title
			titleSlug
			hasVideoSolution
			hasSolution
			topicTags {
				name
				id
				slug
			}
		}
	}
        # allQuestionsCount {
        #   difficulty
        #   count
        # }
        matchedUser(username: $username) {
          contributions {
            points
          }
        #   profile {
        #     reputation
        #     ranking
        #   }
        #   submissionCalendar
        #   submitStats {
        #     acSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #     }
        #     totalSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #     }
        #   }
        }
        recentSubmissionList(username: $username) {
          title
          titleSlug
          timestamp
          statusDisplay
          lang
          __typename
        }
        # matchedUserStats: matchedUser(username: $username) {
        #   submitStats: submitStatsGlobal {
        #     acSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #       __typename
        #     }
        #     totalSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #       __typename
        #     }
        #     __typename
        #   }
        # }
        
      }
    """

    variables = {"username": username}
    response = requests.post(
        url, headers=headers, json={"query": query, "variables": variables}
    )
    content = response.json()
    current_coins = content["data"]["matchedUser"]["contributions"]["points"]
    # print(points)
    return current_coins


if __name__ == "__main__":
    points = get_points()
    print(points)
