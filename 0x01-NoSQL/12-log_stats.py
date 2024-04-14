#!/usr/bin/env python3
'''
generate log stats from an nginx log file stored in mongodb
'''
from pymongo import MongoClient
client = MongoClient()

db = client.logs

docs_count = db.nginx.count_documents({})
