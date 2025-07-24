from flask import Flask, request, jsonify

app = Flask(__name__)

users = [] 

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        data = request.get_json()
        users.append(data)
        return jsonify({"message": "User added successfully", "user": data}), 201
    else: 
        return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
