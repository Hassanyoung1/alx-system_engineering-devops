#!/usr/bin/python3
"""Import modules"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number
    of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
