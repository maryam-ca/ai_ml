📘 Task 4 – Python Libraries & Packaging
🔰 Introduction

This task is part of Week 1 Python assignments.
It focuses on learning how to build clean, modular, and production-ready Python projects.

The main purpose of this task is to help learners understand how real-world Python projects are structured.
It introduces important concepts such as:

Modules

Virtual environments

Custom Python packages

Logging

Dependency management

These practices are very important for professional Python development.

🎯 Objectives of This Task

The objectives of this task are:

To understand modular programming in Python

To learn how to create and use a virtual environment

To understand dependency management using requirements.txt

To create and use a custom Python package

To learn basic logging for production-ready code

⭐ Key Features
🔹 Modular Programming

Python code is divided into multiple modules

Each module performs only one responsibility

Modules are reused using proper import statements

This makes the code:

Clean

Reusable

Easy to maintain

🔹 Virtual Environment

A virtual environment (venv) is used to isolate the project.

Benefits:

Prevents dependency conflicts

Keeps project dependencies separate

Provides a clean development environment

🔹 Custom Python Package

A custom package named mypackage is created

Proper folder structure is followed

__init__.py is used to expose package functions

Package is installed locally using pip install .

This simulates real-world package development.

🔹 Logging

Python’s built-in logging module is used

Logs are written to a file instead of using print()

Makes the application production-ready

Logging helps in:

Debugging

Monitoring

Error tracking

🔹 Clean Project Structure

Logical and readable folder organization

Separate folders for:

Modules

Packages

Tests

Easy to maintain and extend

📂 Project Structure
Task4/
│
├── modules/
│   ├── __init__.py
│   ├── calculator.py
│   ├── string_utils.py
│   └── file_utils.py
│
├── mypackage/
│   ├── mypackage/
│   │   ├── __init__.py
│   │   ├── math_ops.py
│   │   ├── text_ops.py
│   │   └── logger.py
│   │
│   ├── setup.py
│   └── README.md
│
├── test_modules.py
├── test_package.py
├── requirements.txt
└── README.md


📌 Each file and folder has a clear responsibility.

▶️ How to Run the Project
Step 1: Create Virtual Environment
python -m venv venv

Step 2: Activate Virtual Environment (Windows)
venv\Scripts\activate


After activation, (venv) will appear in the terminal.

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Install Custom Package
cd mypackage
pip install .

Step 5: Run Test File
cd ..
python test_package.py

✅ Expected Output
20
nohtyp


This output confirms that:

The package is installed correctly

Imports are working

Functions are executing properly

🧪 Testing

test_modules.py tests modular scripts

test_package.py tests the custom Python package

Successful execution confirms:

Correct project structure

Proper imports

Clean setup

🏁 Conclusion

This task demonstrates how professional Python projects are structured.

It provides hands-on experience with:

Modular programming

Virtual environments

Custom package creation

Dependency management

Logging

Clean project organization

These skills are essential for real-world Python development.

✍️ Author

Maryam Fatima
