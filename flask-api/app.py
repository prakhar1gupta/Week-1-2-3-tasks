from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection string
client = MongoClient("mongodb://localhost:27017")
db = client['mydb']
users_collection = db['users']

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    result = users_collection.insert_one(data)
    return jsonify({'inserted_id': str(result.inserted_id)}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))  # Don't show _id
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
