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

Key Features
Modular Programming

Python code is divided into multiple modules

Each module performs a single responsibility

Modules are reused using proper import statements

Virtual Environment

A virtual environment (venv) is used to isolate the project

Prevents dependency conflicts between projects

Ensures a clean development environment

Custom Python Package

A custom Python package named mypackage is created

Proper folder structure is followed

__init__.py is used to expose package functions

Package is installed locally using pip install .

Logging

Python’s built-in logging module is used

Logs are written to a file instead of using print

Makes the project production-ready

Clean Project Structure

Logical and readable folder organization

Separate folders for modules, package, and tests

Easy to maintain and extend

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

How to Run the Project
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

Expected Output
20
nohtyp


This confirms that the package is installed and working correctly.

Testing

test_modules.py tests modular scripts

test_package.py tests the custom Python package

Successful execution confirms correct imports and setup

Conclusion

This task demonstrates how Python projects are structured in professional environments.
It provides hands-on experience with modular programming, package creation, dependency management, and clean project organization.

Author

Maryam Fatima
