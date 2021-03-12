from sql_database import SQLDatabase
import json
import datetime

def get_data(event, context):
    
    #print(event['body'])
    db = SQLDatabase()

    data = []

    for b in event['body']:
        #print(b['type'])

        sql = get_sql(b['type'], b['select'], 
                      b['from'], b['where'], 
                      b['order'])

        #print(sql)

        data.append(db.retrieve_sql_data(sql))

    #print(data)

    db.disconnect()

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
          'Access-Control-Allow-Origin': '*'
        },
        "body": json.dumps(data, cls=DateTimeEncoder)
    }

    return response

def get_sql(type, select, table, where, order):
    types_allowed = ['normal', 'unique']
    tables_allowed = ['duration', 'form', 'industry', 
                     'occupation', 'sector', 'role']

    if type not in types_allowed:
        return 'Type Error'

    if table not in tables_allowed:
        return 'Table Error'


    sqls = {
        'normal' : """
                    SELECT %s
                    FROM %s
                    WHERE %s
                    ORDER BY %s
                    """ %(select, table, where, order),
        'unique' : """
                    SELECT DISTINCT %s
                    FROM %s
                    ORDER BY %s
                    """ %(select, table, order)
    }
    return sqls[type]

# subclass JSONEncoder
class DateTimeEncoder(json.JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()