#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
        """prints the titles of the top ten hot posts for a given subreddit"""
            if subreddit is None or type(subreddit) is not str:
                        print(None)
                            r = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
        print(None)
    else:
