import json
import os

DATA_FILE = "data/students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(student):
    students = load_students()

    # Check duplicate ID
    for s in students:
        if s["id"] == student["id"]:
            raise ValueError("Student ID already exists")

    students.append(student)
    save_students(students)


def delete_student(student_id):
    students = load_students()
    updated_students = [s for s in students if s["id"] != student_id]

    if len(students) == len(updated_students):
        raise ValueError("Student not found")

    save_students(updated_students)


def get_all_students():
    return load_students()

def update_student(student_id, updated_data):
    students = load_students()
    found = False

    for s in students:
        if s["id"] == student_id:
            s.update(updated_data)
            found = True
            break

    if not found:
        raise ValueError("Student not found")

    save_students(students)


def search_students(query):
    students = load_students()
    query = query.lower()

    return [
        s for s in students
        if query in s["id"].lower() or query in s["name"].lower()
    ]
