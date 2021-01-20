import os
from flask import Flask
import psycopg2
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


app = Flask(__name__)


@app.route('/api')
def api():
    return 'API is working'


if __name__ == "__main__":
    app.run(debug=True)
