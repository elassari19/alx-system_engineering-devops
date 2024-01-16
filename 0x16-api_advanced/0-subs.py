#!/usr/bin/python3
"""
module Reddit API url restfull
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    should return numver of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    response = get('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    if (not response.ok):
        return 0
    
    results = response.json()
    count = results.get('data').get('subscribers')
    return count
