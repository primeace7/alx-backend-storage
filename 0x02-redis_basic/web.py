#!/usr/bin/env python3
'''tracking number of GET requests to a url'''

import requests
import redis
r = redis.Redis()


def get_page(url: str) -> str:
    '''fetch the HTML content of a web page
    and track number of requests to the url
    '''

    response = requests.get(url).text
    key = f'count:{url}'
    r.incr(key, 1)
    r.expire(key, 10)
    return response
