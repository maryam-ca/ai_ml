import streamlit as st
import streamlit.components.v1 as components
import csv
from io import StringIO

from student import Student
from storage import (
    add_student, delete_student,
    get_all_students, update_student, search_students
)

from ui_layout import load_theme, render_header, render_menu

st.set_page_config(page_title="Student Management App", layout="wide")

# ================= LOAD UI =================
load_theme()
render_header()
menu = render_menu()

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
            add_student(Student(sid, name, age, dept).to_dict())
            st.success("🎉 Student added successfully")
        except ValueError as e:
            st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)

# ================= VIEW =================
elif menu == "View Students":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 All Students")

    if students:
        rows = "".join(
            f"<tr><td>{s['id']}</td><td>{s['name']}</td><td>{s['age']}</td><td>{s['department']}</td></tr>"
            for s in students
        )

        components.html(f"""
<style>
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
    color: #e5e7eb;
  }}
  thead tr {{
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    position: sticky;
    top: 0;
    z-index: 2;
  }}
  thead th {{
    padding: 14px;
    text-align: left;
    color: white;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}
  tbody tr {{
    background: rgba(255,255,255,0.06);
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  tbody tr:hover {{
    background: rgba(37,99,235,0.18);
  }}
  tbody td {{
    padding: 12px 14px;
  }}
</style>

<div style="max-height:520px; overflow-y:auto; border-radius:14px;">
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
      {rows}
    </tbody>
  </table>
</div>
""", height=560)

    else:
        st.info("No students found")

    st.markdown('</div>', unsafe_allow_html=True)


# ================= CSV =================
elif menu == "Import CSV":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📂 Import CSV")

    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        reader = csv.DictReader(StringIO(uploaded.getvalue().decode()))
        rows = list(reader)
        st.table(rows)

        if st.button("Add to System"):
            added = skipped = 0
            for r in rows:
                try:
                    add_student(
                        Student(
                            r["student_id"],
                            r["full_name"],
                            int(r["age"]),
                            r["department"]
                        ).to_dict()
                    )
                    added += 1
                except:
                    skipped += 1

            st.success(f"Added: {added}, Skipped: {skipped}")

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
            st.success("Updated successfully")
        except ValueError as e:
            st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)

# ================= SEARCH =================
elif menu == "Search":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Search Student")

    q = st.text_input("Search by ID, Name or Department")

    if q:
        results = search_students(q)

        if results:
            for s in results:
                st.markdown(f"""
                <div style="
                  background: linear-gradient(
                    135deg,
                    rgba(255,255,255,0.10),
                    rgba(255,255,255,0.04)
                  );
                  border-radius: 22px;
                  padding: 26px 32px;
                  margin-top: 22px;
                  border: 1px solid rgba(255,255,255,0.18);
                  box-shadow: 0 18px 45px rgba(0,0,0,.55);
                ">

                  <!-- HEADER -->
                  <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                    <span style="font-size:1.6rem;">🎓</span>
                    <h3 style="margin:0;">{s['name']}</h3>
                  </div>

                  <hr style="border:0; height:1px; background:rgba(255,255,255,0.15); margin:12px 0 18px 0;">

                  <!-- DETAILS GRID -->
                  <div style="
                    display:grid;
                    grid-template-columns: 1fr 1fr;
                    row-gap:14px;
                    column-gap:30px;
                    font-size:0.95rem;
                  ">
                    <div><b>🆔 Student ID</b><br>{s['id']}</div>
                    <div><b>🎂 Age</b><br>{s['age']}</div>
                    <div><b>🏫 Department</b><br>{s['department']}</div>
                  </div>

                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No student found")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= DELETE =================
elif menu == "Delete":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🗑 Delete Student")

    sid = st.text_input("Student ID")
    if st.button("Delete"):
        try:
            delete_student(sid)
            st.success("Deleted successfully")
        except ValueError as e:
            st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)
