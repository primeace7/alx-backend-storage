#!/usr/bin/env python3
'''return a list of students from a collection sorted based
on calculated averages
'''
import pymongo


def top_students(mongo_collection):
    '''sort a collection of student students based on
    their calculated and inserted scores
    '''
    all_students = mongo_collection.find()

    for student in all_students:
        total_score = 0
        total_topics = len(student.get('topics'))
        for topic in student.get('topics'):
            total_score += topic.get('score')
        average_score = total_score / total_topics
        mongo_collection.update_one({'name': student.get('name')},
                                    {'$set': {'averageScore': average_score}})

    updated_students = mongo_collection.find(sort=[('averageScore', pymongo.DESCENDING)])
    return updated_students
