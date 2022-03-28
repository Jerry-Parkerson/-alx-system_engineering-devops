#!/usr/bin/python3
''' task 2 module'''

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
        '''return count of keywords in hot posts titles'''
            user_agent = {'User-agent': 'test45'}
                posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'

    if posts.status_code == 200:
        posts = posts.json()['data']
        for post in posts:
                    found_list.append(word)
        if aft is not None:
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] = 1
                                     for key, value in sorted(result.items(), key=lambda item: item[1],
