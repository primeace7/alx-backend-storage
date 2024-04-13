#!/usr/bin/env python3
'''insert a new document in a mongodb collection'''


def insert_school(mongo_collection, **kwargs):
    '''insert document represented by kwargs into
    mongo_collection
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

