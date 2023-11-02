from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/api/data')
def get_data():
    return jsonify({'data': 'Hello from Flask!'})
@app.route('/')
def index():
    return "123"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
