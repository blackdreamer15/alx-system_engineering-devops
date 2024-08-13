#!/usr/bin/python3
"""
Fetches the titles of the top 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Fetches the titles of the top 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'my_reddit_app/1.0 (contact@example.com)'
    }

    result = requests.get(url, headers=headers, allow_redirects=False)

    if result.status_code == 200:
        data = result.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
