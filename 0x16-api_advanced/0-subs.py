#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'reddit_api/0-subs/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
      data = response.json()
      return data.get('data', {}).get('subscribers', 0)

    else:
      return 0
