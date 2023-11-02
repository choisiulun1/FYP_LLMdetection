from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5001", "http://127.0.0.1:5001"]}})

@app.route('/api/data')
def get_data():
    return jsonify({'data': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True)
