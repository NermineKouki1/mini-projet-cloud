from flask import Flask, request, jsonify
import psycopg2
import time

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="tasks",
        user="admin",
        password="admin"
    )
    return conn

def init_db():
    for i in range(10):
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully")
            return
        except Exception as e:
            print(f"Database not ready yet, retrying... ({e})")
            time.sleep(2)

init_db()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM tasks ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1]
        })

    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title;",
        (data["title"],)
    )
    new_task = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "id": new_task[0],
        "title": new_task[1]
    }), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Task deleted"})

@app.route('/')
def home():
    return "TODO Service is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)