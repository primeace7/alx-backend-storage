#!/usr/bin/env python3
'''
update a document in a mongodb collection
'''


def update_topics(mongo_collection, name, topics):
    '''update a document with name 'name' in
    mongo_collection by appending topics list
    '''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
