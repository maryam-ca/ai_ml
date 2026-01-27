# student_records.py
# Student Record System

students = []


def add_student(student_id, name, marks):
    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully.")


def update_student(student_id, new_marks):
    for student in students:
        if student["id"] == student_id:
            student["marks"] = new_marks
            print("Student updated successfully.")
            return
    print("Student not found.")


def display_students():
    if not students:
        print("No student records.")
        return
    for student in students:
        print(student)


# Testing
add_student(1, "Ali", 85)
add_student(2, "Sara", 90)
update_student(1, 88)
display_students()
