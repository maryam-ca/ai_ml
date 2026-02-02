🎓 Student Management System

A Streamlit-based Web Application

📌 Project Overview

The Student Management System is a web-based application developed using Python and Streamlit to manage student records efficiently.
It allows users to add, view, search, update, delete, and import students via CSV, all within a clean and modern interface.

This project is designed keeping real-world academic record management in mind and is suitable for university projects and demonstrations.

🚀 Key Features
👤 Student Record Management

Add new student records

Update existing student information

Delete students from the system

Search students by ID, Name, or Department

📂 CSV Import System

Upload CSV files to add students in bulk

Automatically validates and stores records

Supports large datasets efficiently

📋 View All Students

Displays all students in a scrollable table

Supports unlimited (infinite) student records

Sticky table header for better readability

Clean and professional UI

🔍 Advanced Search

Quick search functionality

Displays results in a student profile card

User-friendly and visually appealing output

🖥️ Technologies Used

Python

Streamlit

HTML & CSS (for UI/UX)

CSV (bulk data handling)

JSON (data storage)

📁 Project Structure
Student-Management-System/
│
├── app.py                # Main application logic
├── ui_layout.py          # UI styling & layout
├── student.py            # Student model
├── storage.py            # Data handling logic
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
│
├── assets/
│   └── header.jpg        # Header image
│
├── screenshots/
│   ├── dashboard.png
│   ├── add_student.png
│   ├── view_students.png
│   ├── search_student.png
│   └── import_csv.png
│
└── data/
    └── students.json     # Stored student data

📸 Application Screenshots
🏠 Dashboard

➕ Add Student

📋 View Students

🔍 Search Student

📂 Import CSV

📄 CSV File Format

The system supports CSV files with the following structure:

student_id,full_name,age,department
S001,Ali Ahmed,18,Computer Science
S002,Ayesha Khan,19,Information Technology
S003,Usman Raza,20,Software Engineering

▶️ How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Application
streamlit run app.py

3️⃣ Open in Browser
http://localhost:8501

🌐 Deployment
🚀 Live Deployment

This application has been successfully deployed using Streamlit Cloud, making it accessible online without any local setup.

🔗 Live Demo:

https://your-app-name.streamlit.app


(Replace with your actual deployed URL)

✅ Deployment Benefits

Accessible from anywhere

No local installation required

Ideal for project demo & evaluation

Real-world SaaS-like experience

🎯 Project Highlights

Modern dark-theme UI

Handles large datasets

Real-world inspired design

Clean code structure

Fully deployed web application

Perfect for Final Year Project / Mini Project

📌 Future Enhancements

User authentication (Admin / Staff)

Database integration (MySQL / PostgreSQL)

Export student data (CSV / Excel)

Pagination and advanced filters

Role-based access control

👩‍💻 Developed By

Maryam Fatima
Computer Science Student

📜 License

This project is developed for educational purposes only.
