#!/usr/bin/python3
'''
module Reddit API url restfull
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''
Reddit's API url restfull
'''


def top_ten(subreddit):
    '''
    should return the title of ten posts
    '''
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        print(None)
        return
    req = req.json()
    if "data" in req:
        for post in req.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
