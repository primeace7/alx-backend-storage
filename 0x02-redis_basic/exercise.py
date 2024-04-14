#!/usr/bin/env python3
'''
Working with redis as a basic cache
'''
import redis
import uuid
from functools import wraps
from typing import Union, Callable


def call_history(method: Callable) -> Callable:
    '''store inputs and outputs history of a method in redis'''
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        result = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', result)
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    '''decorator to count the number of times a method is called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__, 1)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache:
    '''
    a simple cache class with basic redis functionality
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store a value in the redis db'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return f'{key}'

    def get(self, key: str, fn: Union[Callable, None]) -> Union[
            bytes, int, str, None]:
        '''retrieve a value from the redis db'''
        if not self._redis.exists(key):
            return None

        result = self._redis.get(key)

        if fn is str:
            return self.get_str(key)
        elif fn is int:
            return self.get_int(key)
        elif fn is None:
            return result
        else:
            return fn(result)

    def get_str(self, key):
        '''return a key from redis db as a string'''
        return str(self._redis.get(key))

    def get_int(self, key):
        '''return a key from redis db as an int'''
        return int(self._redis.get(key))


def replay(fn) -> None:
    '''print out all calls of the input function
    with the input and ouput each time
    '''
    db = fn.__self__._redis
    count = db.get(fn.__qualname__)
    qualname = fn.__qualname__
    inputs = db.lrange(f'{fn.__qualname__}:inputs', 0, -1)
    outputs = db.lrange(f'{fn.__qualname__}:outputs', 0, -1)

    print(f'{qualname} was called {int(count)} times')

    for inp, out in zip(inputs, outputs):
        print(f'{qualname}(*{inp.decode("utf-8")})) -> {out.decode("utf-8")}')
