import os
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import json
from flask_cors import CORS

db_host = os.environ['POSTGRESQL_ADDON_HOST']
db_name = os.environ['POSTGRESQL_ADDON_DB']
db_user = os.environ['POSTGRESQL_ADDON_USER']
db_URI = os.environ['POSTGRESQL_ADDON_URI']
db_password = os.environ['POSTGRESQL_ADDON_PASSWORD']

try:
    conn = psycopg2.connect(
        f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{db_password}'")
    print("Database connected")
except:
    print("Not able to connect to Database")


def autocomplete(keyword, limit, offset):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    sql_query = f'''select
                   *
                   from
                   branches
                   where
                   branch like '%{keyword}%'
                   order by ifsc
                   limit {limit} ; '''
    cursor.execute(sql_query)
    record = cursor.fetchall()

    return record


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from heroku'


@app.route('/api/branches/autocomplete')
def api():
    search_query = request.args['q']

    try:
        limit = request.args['limit']
    except:
        limit = 0

    try:
        offset = request.args['offset']
    except:
        offset = 0
    data = {}
    data["branches"] = autocomplete(search_query,limit,offset)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
