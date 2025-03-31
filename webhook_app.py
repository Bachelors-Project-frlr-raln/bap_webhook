from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Store received requests in memory (for simplicity; use a database for production)
requests_list = []

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming request data
    data = request.get_json()
    if data:
        requests_list.append(data)
        print(f"Received webhook data: {json.dumps(data, indent=2)}")
        return jsonify({"message": "Webhook received"}), 200
    return jsonify({"error": "No data received"}), 400

@app.route('/requests', methods=['GET'])
def index():
    # Display all received requests
    return jsonify({"received_requests": requests_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
