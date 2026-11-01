
import sqlite3
import os

ADMIN_PASSWORD = "admin123"

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Defect 1: SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    user = cursor.fetchone()

    # Defect 2: Password is stored and compared as plain text
    if user and user[1] == password:
        return True

    return False


def admin_login(password):
    # Defect 3: Hardcoded admin password
    if password == ADMIN_PASSWORD:
        return True
    return False


def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        # Password is stored without hashing
        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

    except Exception:
        # Defect 4: Exception is silently swallowed
        pass

    conn.close()


def check_login_attempts(username):
    # Defect 5: No rate limiting
    print("Checking login for:", username)
    return True
