#!/usr/bin/python3
"""
Contains the recurse function
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
            """returns a list of all hot post titles for a given subreddit"""
                if subreddit is None or type(subreddit) is not str:
                                return None
                            r = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
            return None
        return hot_list
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
            return None
