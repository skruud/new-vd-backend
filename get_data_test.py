from get_data import *

json_test = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "requestContext": {
        "resourcePath": "/",
        "httpMethod": "GET",
        "path": "/Prod/"
    },
    "headers": {
        "accept": "text/html",
        "accept-encoding": "gzip, deflate, br",
        "Host": "xxx.us-east-2.amazonaws.com",
        "User-Agent": "Mozilla/5.0"
    },
    "body": {
        "select": "amount, date",
        "from": "occupation",
        "where": "location = 'Oslo' AND category = 'IT utvikling'",
        "order": "date"
    }
}

get_data(json_test, 'b')