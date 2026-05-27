import sqlite3
from flask import Flask, request

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded credentials
DB_USER = "admin"
DB_PASS = "password123"  # Never hardcode passwords

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # VULNERABILITY 2: SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect('users.db')
    result = conn.execute(query).fetchone()
    
    # VULNERABILITY 3: No input validation
    if result:
        # VULNERABILITY 4: Sensitive data in response
        return f"Welcome {username}! Your password is {password}"
    else:
        return "Login failed"

@app.route('/search')
def search():
    query = request.args.get('q')
    # VULNERABILITY 5: Cross-Site Scripting XSS
    return f"<h1>Search results for: {query}</h1>"

if __name__ == '__main__':
    # VULNERABILITY 6: Debug mode in production
    app.run(debug=True)