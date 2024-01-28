#!/usr/bin/python3
"""
Module Documentation

Importing in Alphabetical Order

This module provides a function to query the Reddit API and retrieve the number
of subscribers for a given subreddit.

Usage:
    - Import the module.
    - Call the function `number_of_subscribers(subreddit)` with the name of the
    subreddit as the argument.

Example:
    >>> import my_module
    >>> subscribers = my_module.number_of_subscribers("learnpython")
    >>> print(subscribers)
    500000

"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit. If the subreddit is
        invalid or an error occurs during
             the request, returns 0.

    Raises:
        None

    Note:
        This function uses the Requests module for sending HTTP requests to
        the Reddit API.

    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        r.raise_for_status()  # Raise an exception for any HTTP error status
        return r.json()['data']['subscribers']
    except requests.exceptions.RequestException:
        return 0
