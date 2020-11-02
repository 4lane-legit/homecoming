  
import json
import os
import uuid

# TODO
def create(event, context):
    # get request body
    # data = json.loads(event['body'])

    # # create item to insert
    # item = {
    #     '_id': str(uuid.uuid1()),
    #     'data': data,
    # }

    # # write item to database
    # collection.insert_one(item)

    # # create response
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(item)
    # }
    response = 'Here I am this is me!'
    # return response
    return response