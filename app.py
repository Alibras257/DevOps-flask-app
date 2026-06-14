import os
from flask import Flask, jsonify
import psycopg

app = Flask(__name__)

def get_db_connection():
    conn = psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "devops_db"),
        user=os.getenv("DB_USER", "devops_user"),
        password=os.getenv("DB_PASSWORD", "devops_pass")
    )
    return conn

@app.route("/")
def home():
    return "Hello from DevOps Flask App with PostgreSQL!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return jsonify({"database": "connected"})
    except Exception as e:
        return jsonify({"database": "failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
