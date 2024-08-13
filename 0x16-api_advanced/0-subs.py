#!/usr/bin/python3
"""
Module to query the Reddit API
and return the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """Retrieves number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'reddit_api/0-subs/1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0