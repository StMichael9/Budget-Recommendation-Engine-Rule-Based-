"""Handles:

turning results into JSON

turning results into pretty console output

preparing data for future API responses"""

import json

# Squishes data into a tight text line so computers can send it fast
def to_json(data):
    # convert Python dict to JSON string
    data = json.dumps(data)
    return data

# Adds lines and spaces to the text so humans can read it easily
def to_pretty_console(data):
    # convert Python dict to formatted console output
    data = json.dumps(data, indent = 4)
    return data

def to_api_response(data):
    # prepare standardized API response dict
    response = {
        "status": "OK",
        "message": "All right",
        "data": data
    }
    return response