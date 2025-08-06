from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Serve the login page (index.html)
@app.route('/')
def login_page():
    return send_from_directory('.', 'index.html')  # Serve index.html as the login page

# Serve static files (e.g., index22.html, campus-overview.html, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Predefined users categorized by roles
users = {
    "admin": {"john": "123", "nissar": "456"},
    "staff": {"sujith": "123"},
    "student": {"hemanth": "123", "raj": "456", "sita": "789"},
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    role = data.get('role')
    username = data.get('username')
    password = data.get('password')

    if role not in users:
        return jsonify({"message": "Invalid role!"}), 400

    if username in users[role] and users[role][username] == password:
        # Return the role and a success message
        return jsonify({"message": "Login successful!", "role": role}), 200
    else:
        return jsonify({"message": "Invalid username or password!"}), 401

if __name__ == '__main__':
    app.run(debug=True)