import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "../data/students.json")


# ---------------- LOAD ----------------
def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, ValueError):
        return []


# ---------------- SAVE ----------------
def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- ADD ----------------
def add_student(student):
    students = load_students()

    if any(s["id"] == student["id"] for s in students):
        raise ValueError("Student ID already exists")

    students.append(student)
    save_students(students)


# ---------------- DELETE ----------------
def delete_student(student_id):
    students = load_students()
    updated = [s for s in students if s["id"] != student_id]

    if len(updated) == len(students):
        raise ValueError("Student not found")

    save_students(updated)


# ---------------- READ ----------------
def get_all_students():
    return load_students()


# ---------------- UPDATE ----------------
def update_student(student_id, updated_data):
    students = load_students()

    for s in students:
        if s["id"] == student_id:
            s["name"] = updated_data.get("name", s["name"])
            s["age"] = updated_data.get("age", s["age"])
            s["department"] = updated_data.get("department", s["department"])
            save_students(students)
            return

    raise ValueError("Student not found")


# ---------------- SEARCH ----------------
def search_students(query):
    students = load_students()
    query = query.lower().strip()

    return [
        s for s in students
        if query in s["id"].lower()
        or query in s["name"].lower()
        or query in s["department"].lower()
    ]
