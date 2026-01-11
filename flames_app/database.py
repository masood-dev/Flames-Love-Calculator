"""
Database module for Secret Admirer feature
Learning: SQLite is a lightweight database that stores data in a single file
"""

import sqlite3
import secrets
import os
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'secret_notes.db')

def get_db_connection():
    """
    Learning: Connection object lets us execute SQL commands
    We use 'Row' factory to access columns by name (easier than index numbers)
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns like dict: row['message']
    return conn

def init_db():
    """
    Learning: Creates the database table if it doesn't exist
    This runs once when the app starts
    """
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS secret_notes (
            id TEXT PRIMARY KEY,
            message TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            sender_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP,
            view_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def create_note(message, password, sender_name=None, expire_days=30):
    """
    Learning: 
    - secrets.token_urlsafe() generates random unique ID (cryptographically secure)
    - generate_password_hash() uses bcrypt to hash password (one-way, can't reverse)
    - SQL INSERT adds new row to database
    
    Returns: unique note_id for the shareable link
    """
    conn = get_db_connection()
    note_id = secrets.token_urlsafe(8)  # Generates ID like: "xK7mP9qR"
    password_hash = generate_password_hash(password)
    expires_at = datetime.now() + timedelta(days=expire_days)
    
    conn.execute('''
        INSERT INTO secret_notes (id, message, password_hash, sender_name, expires_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (note_id, message, password_hash, sender_name, expires_at))
    
    conn.commit()
    conn.close()
    return note_id

def get_note(note_id):
    """
    Learning: SQL SELECT retrieves data
    Returns note data (without password for security)
    """
    conn = get_db_connection()
    note = conn.execute(
        'SELECT id, message, sender_name, created_at, view_count FROM secret_notes WHERE id = ?',
        (note_id,)
    ).fetchone()
    conn.close()
    return note

def verify_password(note_id, password):
    """
    Learning: check_password_hash() compares entered password with stored hash
    This is secure - we never store the actual password!
    """
    conn = get_db_connection()
    note = conn.execute(
        'SELECT password_hash FROM secret_notes WHERE id = ?',
        (note_id,)
    ).fetchone()
    
    if note and check_password_hash(note['password_hash'], password):
        # Increment view count
        conn.execute(
            'UPDATE secret_notes SET view_count = view_count + 1 WHERE id = ?',
            (note_id,)
        )
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False

def cleanup_expired_notes():
    """
    Learning: Deletes notes older than expiration date
    Could run this periodically or on app startup
    """
    conn = get_db_connection()
    conn.execute('DELETE FROM secret_notes WHERE expires_at < ?', (datetime.now(),))
    conn.commit()
    conn.close()
