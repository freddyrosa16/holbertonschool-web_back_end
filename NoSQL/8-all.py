#!/usr/bin/env python3
""" function that lists all documents in a collection """


def list_all(mongo_collection):
    """ listing all collections """
    if mongo_collection is not None:
        document = mongo_collection.find()
        return list(document) if document else []
    return []
