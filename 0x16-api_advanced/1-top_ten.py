#!/usr/bin/python3
""" Import modules """
import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for
    a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    header = {'user-agent': 'X-Modhash'}
    if subreddit is None:
        print(None)
    try:
        req = requests.get(url, headers=header, allow_redirects=False)
        data = req.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    except BaseException:
        print(None)
