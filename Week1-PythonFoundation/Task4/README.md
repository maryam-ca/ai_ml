Task 4 – Python Libraries & Packaging
Introduction

This task is part of Week 1 Python assignments and focuses on learning how to build clean, modular, and production-ready Python projects.

The main purpose of this task is to help learners understand how Python projects are structured in real-world development using modules, virtual environments, custom packages, and logging.

This task also introduces best practices such as dependency management, clean folder organization, and proper documentation, which are essential for professional Python development.

Objectives of This Task

To understand modular programming in Python

To learn how to create and use a virtual environment

To understand dependency management using requirements.txt

To create and use a custom Python package

To learn basic logging for production-ready code

To follow clean and professional project structure

Key Features
Modular Programming

Python code is divided into multiple modules, where each module performs a specific task.
This makes the code reusable, readable, and easy to maintain.

Virtual Environment

A virtual environment (venv) is used to isolate the project dependencies.
This helps avoid conflicts between different Python projects and ensures a clean development environment.

Custom Python Package

A custom Python package named mypackage is created using proper packaging standards.
The package includes multiple modules and uses __init__.py to expose required functionality.
The package is installed locally using pip install ..

Logging

Python’s built-in logging module is used instead of print statements.
Logs are stored in a file, making the project more suitable for real-world and production use.

Clean Project Structure

The project follows a clean and logical folder structure.
Separate folders are used for modules, packages, tests, and documentation, making the project easy to understand and extend.

Project Structure
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

How to Run This Project
Step 1: Create Virtual Environment
python -m venv venv

Step 2: Activate Virtual Environment

For Windows

venv\Scripts\activate


After activation, (venv) will appear in the terminal.

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Install Custom Package

Navigate to the mypackage folder:

cd mypackage
pip install .

Step 5: Run Test Files

Go back to the Task4 folder:

cd ..
python test_package.py

Expected Output
20
nohtyp


This output confirms that the custom package is installed correctly and working as expected.

Testing

test_modules.py is used to test modular scripts

test_package.py is used to test the custom Python package

Successful execution confirms correct imports and package installation

Conclusion

This task demonstrates how Python projects are developed in a professional environment.
By completing this task, learners gain practical experience in modular programming, package creation, dependency management, and clean code organization.

Author

Maryam Fatima
