#!/usr/bin/env python3
""" function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ function that returns new id """
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
    else:
        return None
