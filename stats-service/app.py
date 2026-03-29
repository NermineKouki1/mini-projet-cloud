from flask import Flask, jsonify
import redis
import time

app = Flask(__name__)

def get_redis_connection():
    return redis.Redis(host='redis', port=6379, decode_responses=True)

def init_redis():
    for i in range(10):
        try:
            r = get_redis_connection()
            r.ping()
            print("Redis connected successfully")
            return
        except Exception as e:
            print(f"Redis not ready yet, retrying... ({e})")
            time.sleep(2)

init_redis()

@app.route('/')
def home():
    return "Stats Service is running"

@app.route('/stats', methods=['GET'])
def get_stats():
    r = get_redis_connection()
    visits = r.incr('visits')
    return jsonify({"visits": visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)