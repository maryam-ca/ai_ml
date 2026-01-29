📘 TASK 4 – PYTHON LIBRARIES & PACKAGING
🔰 INTRODUCTION

This task is part of Week 1 Python assignments and focuses on learning how to build clean, modular, and production-ready Python projects.

The main purpose of this task is to help learners understand how real-world Python projects are structured using:

Modules

Virtual environments

Custom Python packages

Logging

This task also introduces best practices such as dependency management, clean folder organization, and proper documentation, which are essential for professional Python development.

🎯 OBJECTIVES OF THIS TASK

The objectives of this task are:

To understand modular programming in Python

To learn how to create and use a virtual environment

To understand dependency management using requirements.txt

To create and use a custom Python package

To learn basic logging for production-ready code

⭐ KEY FEATURES
🔹 MODULAR PROGRAMMING

Python code is divided into multiple modules

Each module performs a single responsibility

Modules are reused using proper import statements

This approach makes the code:

Clean

Reusable

Easy to maintain

🔹 VIRTUAL ENVIRONMENT

A virtual environment (venv) is used to isolate the project.

Benefits:

Prevents dependency conflicts

Keeps project libraries separate

Ensures a clean development environment

🔹 CUSTOM PYTHON PACKAGE

A custom Python package named mypackage is created

Proper folder structure is followed

__init__.py is used to expose package functions

Package is installed locally using pip install .

This simulates real-world Python package development.

🔹 LOGGING

Python’s built-in logging module is used

Logs are written to a file instead of using print()

Makes the application production-ready

Logging helps in:

Debugging

Error tracking

Monitoring application behavior

🔹 CLEAN PROJECT STRUCTURE

Logical and readable folder organization

Separate folders for:

Modules

Packages

Tests

Easy to maintain and extend

📂 PROJECT STRUCTURE
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


Each file and folder has a clear and specific responsibility.

▶️ HOW TO RUN THE PROJECT
✅ STEP 1: CREATE VIRTUAL ENVIRONMENT
python -m venv venv

✅ STEP 2: ACTIVATE VIRTUAL ENVIRONMENT (WINDOWS)
venv\Scripts\activate


After activation, (venv) will appear in the terminal.

✅ STEP 3: INSTALL DEPENDENCIES
pip install -r requirements.txt

✅ STEP 4: INSTALL CUSTOM PACKAGE
cd mypackage
pip install .

✅ STEP 5: RUN TEST FILE
cd ..
python test_package.py

📤 EXPECTED OUTPUT
20
nohtyp


This confirms that:

The package is installed correctly

Imports are working properly

Functions are executing as expected

🧪 TESTING

test_modules.py is used to test modular scripts

test_package.py is used to test the custom Python package

Successful execution confirms:

Correct imports

Proper setup

Clean project structure

🏁 CONCLUSION

This task demonstrates how professional Python projects are structured.

It provides practical experience with:

Modular programming

Virtual environments

Custom package creation

Dependency management

Logging

Clean project organization

These concepts are essential for real-world Python development.

✍️ AUTHOR

Maryam Fatima
