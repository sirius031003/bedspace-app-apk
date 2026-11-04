"""
BedSpace Dormitory - Client / Tenant Mobile Application
Built for Python & VS Code (Compatible with Windows, Mac, Linux, and APK)
"""
import sqlite3
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# SQLite Database Initialization (Flowchart: Initializing Database)
DB_NAME = "bedspace.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        password TEXT NOT NULL,
        room_id INTEGER,
        bed_slot TEXT
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_number TEXT NOT NULL,
        floor TEXT NOT NULL,
        type TEXT NOT NULL,
        rate REAL NOT NULL,
        capacity INTEGER NOT NULL,
        occupied INTEGER NOT NULL,
        status TEXT NOT NULL,
        owner_contact TEXT NOT NULL
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS dues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        method TEXT NOT NULL,
        ref_number TEXT,
        payment_date TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database ready. Starting BedSpace Mobile App...")
    # Tkinter mobile frame launcher...
