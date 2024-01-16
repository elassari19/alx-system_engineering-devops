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
    header = {'User-Agent': 'CustomClient/1.0'}
    res = requests.get(BASE_URL+"/r/{}?sort=hot&limit=10".format(subreddit),
                       headers=header, allow_redirects=False)
    if res.status_code != 200:
        return (0)
    res = res.json()
    if "data" in res:
        for post in res.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)