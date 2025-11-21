from flask import Flask, request, render_template, redirect, url_for, flash, session
import mysql.connector
import hashlib
import os

app = Flask(__name__)
app.secret_key = "this-is-a-secret-key"


# -----------------------------------------
# DATABASE CONNECTION
# -----------------------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parth@2310",
        database="flask_auth"
    )


# -----------------------------------------
# PASSWORD HASHING (SHA256)
# -----------------------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -----------------------------------------
# HOME PAGE
# -----------------------------------------
@app.route('/')
def home():
    return render_template("home_new.html", title="Home")


# -----------------------------------------
# REGISTER PAGE + LOGIC
# -----------------------------------------
@app.route('/register')
def register_page():
    return render_template("register.html", title="Register")


@app.route('/register_post', methods=['POST'])
def register_post():
    username = request.form.get("username")
    password = request.form.get("password")

    # Validation
    if not username or not password:
        flash("Please fill all fields!", "error")
        return redirect(url_for('register_page'))

    hashed = hash_password(password)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if username exists
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing = cursor.fetchone()

        if existing:
            flash("Username already exists!", "error")
            return redirect(url_for('register_page'))

        # Insert new user
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed)
        )
        conn.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login_page'))

    except Exception as e:
        flash(f"Error: {e}", "error")
        return redirect(url_for('register_page'))


# -----------------------------------------
# LOGIN PAGE + AUTH LOGIC
# -----------------------------------------
@app.route('/login')
def login_page():
    return render_template("login.html", title="Login")


@app.route('/login_db', methods=['POST'])
def login_db():
    username = request.form.get("username")
    password = request.form.get("password")

    # Validation
    if not username or not password:
        flash("Please fill all fields!", "error")
        return redirect(url_for('login_page'))

    hashed_input = hash_password(password)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check username
        cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        row = cursor.fetchone()

        if not row:
            flash("User does not exist!", "error")
            return redirect(url_for('login_page'))

        stored_hash = row[0]

        # Password check
        if hashed_input != stored_hash:
            flash("Incorrect password!", "error")
            return redirect(url_for('login_page'))

        # SUCCESS LOGIN
        session['user'] = username
        flash("Login successful!", "success")
        return redirect(url_for('dashboard'))

    except Exception as e:
        flash(f"Error: {e}", "error")
        return redirect(url_for('login_page'))


# -----------------------------------------
# DASHBOARD (Protected Route)
# -----------------------------------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash("Please login first!", "error")
        return redirect(url_for('login_page'))

    return render_template("dashboard.html", title="Dashboard")

#--------------------------
# Profile page 
#---------------------------
@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login_page'))

    username = session['user']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        return render_template("profile.html", user=user[0], title="Profile")

    except Exception as e:
        return f"Error: {e}"

# -----------------------------------------
# LOGOUT
# -----------------------------------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('login_page'))


# -----------------------------------------
# RUN APPLICATION
# -----------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
