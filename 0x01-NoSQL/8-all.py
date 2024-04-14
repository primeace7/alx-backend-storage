#!/usr/bin/env python3
""" list all documents in a mongo db collection """


def list_all(mongo_collection):
    '''return a list of all documents
    in a collection'''
    return mongo_collection.find()
