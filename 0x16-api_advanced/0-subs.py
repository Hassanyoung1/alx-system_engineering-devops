#!/usr/bin/python3
def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number
    of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.
    """
    import requests
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
