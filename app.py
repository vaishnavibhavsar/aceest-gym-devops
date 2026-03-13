from flask import Flask, jsonify, request

app = Flask(__name__)

members = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    member = {
        "name": data["name"],
        "membership": data["membership"]
    }
    members.append(member)
    return jsonify(member), 201

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
