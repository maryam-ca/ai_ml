# student_records.py
# Student Record System

from utils import calculate_average

students = []


def add_student(sid, name, marks):
    students.append({"id": sid, "name": name, "marks": marks})


def update_student(sid, marks):
    for s in students:
        if s["id"] == sid:
            s["marks"] = marks
            return
    print("Student not found")


def display_students():
    for s in students:
        print(s)

    marks = [s["marks"] for s in students]
    print("Average Marks:", calculate_average(*marks))


if __name__ == "__main__":
    add_student(1, "Ali", 80)
    add_student(2, "Sara", 90)
    update_student(1, 85)
    display_students()
