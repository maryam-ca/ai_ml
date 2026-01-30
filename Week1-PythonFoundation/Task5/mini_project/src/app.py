import streamlit as st
from student import Student
from storage import add_student, delete_student, get_all_students

st.set_page_config(page_title="Student Management App", layout="centered")

st.title("🎓 Student Management System")
st.write("A simple Streamlit app to manage student records")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students", "Delete Student"]
)

# ---------------- ADD STUDENT ----------------
if menu == "Add Student":
    st.subheader("Add New Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    department = st.text_input("Department")

    if st.button("Add Student"):
        try:
            if not student_id or not name or not department:
                st.error("All fields are required")

            student = Student(student_id, name, age, department)
            add_student(student.to_dict())

            st.success("Student added successfully")

        except ValueError as e:
            st.error(str(e))

# ---------------- VIEW STUDENTS ----------------
elif menu == "View Students":
    st.subheader("All Students")

    students = get_all_students()

    if not students:
        st.info("No students found")
    else:
        for s in students:
            st.write(
                f"🆔 {s['id']} | 👤 {s['name']} | 🎂 {s['age']} | 🏫 {s['department']}"
            )

# ---------------- DELETE STUDENT ----------------
elif menu == "Delete Student":
    st.subheader("Delete Student")

    student_id = st.text_input("Enter Student ID to delete")

    if st.button("Delete"):
        try:
            delete_student(student_id)
            st.success("Student deleted successfully")
        except ValueError as e:
            st.error(str(e))
