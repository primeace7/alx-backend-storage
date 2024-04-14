#!/usr/bin/env python3
'''list all documents in a collection having a specified
value in a specified field'''


def schools_by_topic(mongo_collection, topic):
    '''return a list of all documents with a particular
    topic in hte topic filed
    '''
    result = mongo_collection.find(
        {'topics': {'$elemMatch': {'$in': [topic]}}})
    return result
