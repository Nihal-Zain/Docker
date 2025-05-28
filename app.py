# app.py
from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host=os.environ.get("POSTGRES_HOST")
        )
        return "Connected to the PostgreSQL database!"
    except Exception as e:
        return f"Failed to connect to DB: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
