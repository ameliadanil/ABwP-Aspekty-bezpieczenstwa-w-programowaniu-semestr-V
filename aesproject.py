from flask import Flask, request, render_template_string
import sqlite3
import bcrypt

app = Flask(__name__)

DATABASE = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users') 
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

    admin_password = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt())
    user_password = bcrypt.hashpw("user123".encode('utf-8'), bcrypt.gensalt())

    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', ('admin', admin_password))
    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', ('user', user_password))

    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template_string('''
    <h1>Logowanie</h1>
    <form method="POST" action="/login">
        <label>Username: <input type="text" name="username"></label><br>
        <label>Password: <input type="password" name="password"></label><br>
        <button type="submit">Zaloguj</button>
    </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
        return f"<h1>Witaj, {user[1]}!</h1>"
    else:
        return "<h1>Błędny login lub hasło</h1>"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
