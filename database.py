"""
database.py
-----------
All database logic lives here. Nothing else in the app talks to
SQLite directly — app.py only calls these functions.

Two tables (a real relational design, like your DBMS coursework):

  students            subject_marks
  ------------         ------------------
  id (PK)     <----+   id (PK)
  name              +--student_id (FK -> students.id)
  age                   subject
  total_marks           marks
  percentage
  grade
  result
  created_at
"""

import sqlite3
from datetime import datetime

DB_NAME = "students.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            total_marks INTEGER NOT NULL,
            percentage REAL NOT NULL,
            grade TEXT NOT NULL,
            result TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS subject_marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            marks INTEGER NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    """)

    conn.commit()
    conn.close()


def add_student(name, age, subjects, marks, total_marks, percentage, grade, result):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, age, total_marks, percentage, grade, result, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, total_marks, percentage, grade, result, datetime.now().strftime("%Y-%m-%d %H:%M")))

    student_id = cur.lastrowid

    for sub, mark in zip(subjects, marks):
        cur.execute("""
            INSERT INTO subject_marks (student_id, subject, marks)
            VALUES (?, ?, ?)
        """, (student_id, sub, mark))

    conn.commit()
    conn.close()
    return student_id


def get_student_by_id(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cur.fetchone()

    cur.execute("SELECT subject, marks FROM subject_marks WHERE student_id = ?", (student_id,))
    subjects = cur.fetchall()

    conn.close()
    return student, subjects


def get_all_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY id DESC")
    students = cur.fetchall()
    conn.close()
    return students


def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM subject_marks WHERE student_id = ?", (student_id,))
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
