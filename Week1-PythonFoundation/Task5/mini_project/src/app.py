import streamlit as st
import streamlit.components.v1 as components
from student import Student
from storage import (
    add_student, delete_student,
    get_all_students, update_student, search_students
)
import base64
import os

# ✅ STEP 1 — CSV Reader Logic (Backend Helper)
import csv
from io import StringIO


st.set_page_config(page_title="Student Management App", layout="wide")

# ================= IMAGE HELPER =================
def get_base64_image(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "assets", filename)
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ================= THEME (ENHANCED) =================
st.markdown("""
<style>
:root {
  --primary: #6366f1;
  --secondary: #8b5cf6;
  --glass: rgba(255,255,255,0.14);
  --glass-dark: rgba(0,0,0,0.35);
}

body {
  background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81);
}
.main { background: transparent; }

/* CARDS */
.card {
  background: var(--glass);
  border-radius: 28px;
  padding: 36px;
  margin: 28px auto;
  max-width: 1150px;
  box-shadow: 0 25px 70px rgba(0,0,0,.55);
  backdrop-filter: blur(18px);
}
.card:empty { display: none; }

/* HEADER IMAGE */
.header-img {
  position: relative;
  width: 100%;
  height: 340px;
  border-radius: 32px;
  overflow: hidden;
  margin: 32px auto;
  max-width: 1150px;
  box-shadow: 0 30px 80px rgba(0,0,0,.65);
}
.header-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.header-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    rgba(0,0,0,0.65),
    rgba(0,0,0,0.35)
  );
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.header-text h1 {
  color: white;
  font-size: 44px;
  font-weight: 900;
  letter-spacing: .5px;
}
.header-text p {
  color: #e5e7eb;
  font-size: 16px;
  margin-top: 6px;
}

/* TEXT */
h1, h2, h3, p, label {
  color: white !important;
}

/* MENU PILLS */
div[role="radiogroup"] {
  margin: 18px 0 26px;
}
div[role="radiogroup"] > label {
  background: rgba(255,255,255,.18);
  padding: 14px 32px;
  margin-right: 14px;
  border-radius: 999px;
  font-weight: 600;
  transition: all .25s ease;
}
div[role="radiogroup"] > label:hover {
  background: rgba(255,255,255,.30);
  transform: translateY(-2px);
}

/* INPUTS */
.stTextInput input, .stNumberInput input {
  border-radius: 16px;
  padding: 12px;
}

/* BUTTONS */
.stButton>button {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: white;
  border-radius: 18px;
  height: 50px;
  font-weight: 700;
  border: none;
  transition: .25s ease;
}
.stButton>button:hover {
  transform: scale(1.05);
  box-shadow: 0 16px 40px rgba(99,102,241,.6);
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
img_base64 = get_base64_image("header.jpg")

st.markdown(f"""
<div class="header-img">
  <img src="data:image/jpg;base64,{img_base64}">
  <div class="header-overlay">
    <div class="header-text">
      <h1>🎓 Student Management System</h1>
      <p>Manage • Organize • Track student records efficiently</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ================= MENU =================
menu = st.radio(
    "",
    ["Add Student", "View Students", "Import CSV", "Update Student", "Search", "Delete"],
    horizontal=True
)

# ================= DASHBOARD =================
students = get_all_students()
departments = {s["department"] for s in students}

st.markdown(f"""
<div class="card">
  <h3>📊 Dashboard</h3>
  <p>👥 <b>Total Students:</b> {len(students)}</p>
  <p>🏫 <b>Departments:</b> {len(departments)}</p>
</div>
""", unsafe_allow_html=True)

# ================= ADD =================
if menu == "Add Student":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("➕ Add New Student")

    sid = st.text_input("Student ID")
    name = st.text_input("Full Name")
    age = st.number_input("Age", 1, 100)
    dept = st.text_input("Department")

    if st.button("Add Student"):
        try:
            student = Student(sid, name, age, dept)
            add_student(student.to_dict())
            st.success("🎉 Student added successfully")
        except ValueError as e:
            st.error(str(e))
    st.markdown('</div>', unsafe_allow_html=True)

# ================= VIEW =================
elif menu == "View Students":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 All Students")

    if not students:
        st.info("No students found")
    else:
        table_html = """
        <style>
        table {
          width: 100%;
          border-collapse: collapse;
          background: var(--glass-dark);
          color: white;
          border-radius: 20px;
          overflow: hidden;
          font-size: 15px;
        }
        thead {
          background: linear-gradient(135deg, #6366f1, #8b5cf6);
        }
        th {
          padding: 18px;
          text-align: left;
          font-weight: 800;
        }
        td {
          padding: 18px;
        }
        tbody tr {
          border-bottom: 1px solid rgba(255,255,255,.12);
        }
        tbody tr:hover {
          background: rgba(255,255,255,.14);
        }
        </style>

        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Age</th>
              <th>Department</th>
            </tr>
          </thead>
          <tbody>
        """
        for s in students:
            table_html += f"""
            <tr>
              <td>{s['id']}</td>
              <td>{s['name']}</td>
              <td>{s['age']}</td>
              <td>{s['department']}</td>
            </tr>
            """
        table_html += "</tbody></table>"
        components.html(table_html, height=300)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= CSV IMPORT =================
elif menu == "Import CSV":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📂 Import Students from CSV")

    st.markdown("""
    <p>Upload a CSV file with the following columns:</p>
    <code>id, name, age, department</code>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file:
        try:
            string_data = uploaded_file.getvalue().decode("utf-8")
            csv_file = StringIO(string_data)
            reader = csv.DictReader(csv_file)

            csv_students = list(reader)

            if not csv_students:
                st.warning("CSV file is empty")
                st.stop()

            st.success("CSV file loaded successfully ✅")

            # Preview Table
            st.markdown("### 📋 CSV Preview")
            st.table(csv_students)

            if st.button("➕ Add All Students to System"):
                added = 0
                skipped = 0

                for s in csv_students:
                    try:
                        student = Student(
                            s["id"].strip(),
                            s["name"].strip(),
                            int(s["age"]),
                            s["department"].strip()
                        )
                        add_student(student.to_dict())
                        added += 1
                    except Exception:
                        skipped += 1

                st.success(f"✅ Added: {added} students")
                if skipped:
                    st.warning(f"⚠️ Skipped: {skipped} (duplicates or invalid data)")

        except Exception as e:
            st.error(f"Invalid CSV file: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= UPDATE =================
elif menu == "Update Student":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✏️ Update Student")

    sid = st.text_input("Student ID")
    name = st.text_input("New Name")
    age = st.number_input("New Age", 1, 100)
    dept = st.text_input("New Department")

    if st.button("Update"):
        try:
            update_student(sid, {"name": name, "age": age, "department": dept})
            st.success("✅ Student updated successfully")
        except ValueError as e:
            st.error(str(e))
    st.markdown('</div>', unsafe_allow_html=True)

# ================= SEARCH =================
elif menu == "Search":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Search Students")

    q = st.text_input("Search by ID or Name")
    if q:
        for s in search_students(q):
            st.markdown(
                f"🆔 {s['id']} | 👤 {s['name']} | 🎂 {s['age']} | 🏫 {s['department']}"
            )
    st.markdown('</div>', unsafe_allow_html=True)

# ================= DELETE =================
elif menu == "Delete":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🗑️ Delete Student")

    sid = st.text_input("Student ID")
    if st.button("Delete"):
        try:
            delete_student(sid)
            st.success("🗑️ Student deleted successfully")
        except ValueError as e:
            st.error(str(e))
    st.markdown('</div>', unsafe_allow_html=True)
