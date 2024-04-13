#!usr/bin/env python3
'''
list all documents in a mongodb collection
'''


def list_all(mongo_collection):
    '''return all documents in mongo_collection'''
    return mongo_collection.find()
