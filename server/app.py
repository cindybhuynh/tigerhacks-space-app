from flask import Flask, jsonify
from flask_cors import CORS # Essential for connecting to your frontend!

app = Flask(__name__)
CORS(app) # Enables your frontend to make requests

@app.route('/api/status')
def get_status():
    return jsonify({"status": "Server is Running!", "theme": "Space"})

if __name__ == '__main__':
    # Use a non-default port to avoid conflicts
    app.run(debug=True, port=5000)