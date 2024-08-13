#!/usr/bin/python3
"""Module to query the Reddit API and print the titles of the first 10 hot posts listed for a given subreddit"""
import requests

def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'my_reddit_app/1.0 (contact@example.com)'}

    try:
      response = requests.get(url, headers=headers, allow_redirects=False)

      if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
          print(post.get('data', {}).get('title', ''))
      else:
        print(None)

    except requests.exceptions.RequestException as e:
        print(None)