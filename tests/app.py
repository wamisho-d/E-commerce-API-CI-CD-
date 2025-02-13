from flask import Flask
from flasgger import Swagger
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
swagger = Swagger(app)

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
except Exception as e:
    print(f"Error connecting to database: {e}")

@app.route('/api/status', methods=['GET'])
def status():
    """API Status Check
    ---
    responses:
      200:
        description: API is running
    """
    return {"message": "API is running!"}, 200

if __name__ == "__main__":
    app.run(debug=True)
