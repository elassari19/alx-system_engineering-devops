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

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=user_agent, params={ 'limit': 10 })
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
