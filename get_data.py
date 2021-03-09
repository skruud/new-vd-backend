from sql_database import SQLDatabase
import json

def get_data(event, context):
    
    #print(event['body'])
    db = SQLDatabase()

    b = event['body']

    sql = """
            SELECT %s
            FROM %s
            WHERE %s
            ORDER BY %s
            """ %(b['select'], b['from'], b['where'], b['order'])

    print(sql)

    db_response = db.retrieve_sql_data(sql)

    print(db_response)

    db.disconnect()

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
          'Access-Control-Allow-Origin': '*'
        }
    }

    return response
