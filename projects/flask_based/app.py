import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')  # Use a default value for development

# Dummy user data for demonstration
USER_DATA = {
    'username': 'user',
    'password': 'password'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == USER_DATA['username'] and password == USER_DATA['password']:
        return redirect(url_for('success'))
    else:
        return 'Invalid credentials. Please try again.'

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
