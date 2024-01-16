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

    url = 'https://www.reddit.com/r//about.json'.format(subreddit)
    response = get(url)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
