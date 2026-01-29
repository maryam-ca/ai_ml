# Task 4 – Python Libraries & Packaging

## Introduction

This task is part of Week 1 Python assignments and focuses on learning how to build clean, modular, and production-ready Python projects.

The main purpose of this task is to help learners understand how real-world Python projects are structured using:

- Modules  
- Virtual environments  
- Custom Python packages  
- Logging  

This task also introduces best practices such as dependency management, clean folder organization, and proper documentation, which are essential for professional Python development.

---

## Objectives of This Task

The objectives of this task are:

- To understand modular programming in Python  
- To learn how to create and use a virtual environment  
- To understand dependency management using `requirements.txt`  
- To create and use a custom Python package  
- To learn basic logging for production-ready code  

---

## Key Features

### Modular Programming

Python code is divided into multiple modules.  
Each module performs a single responsibility and is reused using proper import statements.

This approach makes the code:
- Clean  
- Reusable  
- Easy to maintain  

---

### Virtual Environment

A virtual environment (`venv`) is used to isolate the project.

Benefits include:
- Prevents dependency conflicts  
- Keeps project libraries separate  
- Ensures a clean development environment  

---

### Custom Python Package

A custom Python package named `mypackage` is created.

- Proper folder structure is followed  
- `__init__.py` is used to expose package functions  
- Package is installed locally using `pip install .`  

This simulates real-world Python package development.

---

### Logging

Python’s built-in `logging` module is used.

- Logs are written to a file instead of using `print()`  
- Makes the application production-ready  

Logging helps in:
- Debugging  
- Error tracking  
- Monitoring application behavior  

---

### Clean Project Structure

The project follows a logical and readable folder organization with separate folders for:
- Modules  
- Packages  
- Tests  

This makes the project easy to maintain and extend.

---

## Project Structure

Task4/
│
├── modules/
│ ├── init.py
│ ├── calculator.py
│ ├── string_utils.py
│ └── file_utils.py
│
├── mypackage/
│ ├── mypackage/
│ │ ├── init.py
│ │ ├── math_ops.py
│ │ ├── text_ops.py
│ │ └── logger.py
│ │
│ ├── setup.py
│ └── README.md
│
├── test_modules.py
├── test_package.py
├── requirements.txt
└── README.md


Each file and folder has a clear and specific responsibility.

---

## How to Run the Project

### Step 1: Create Virtual Environment
```bash
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
This confirms that:

The package is installed correctly

Imports are working properly

Functions are executing as expected

Testing
test_modules.py is used to test modular scripts

test_package.py is used to test the custom Python package

Successful execution confirms:

Correct imports

Proper setup

Clean project structure

Conclusion
This task demonstrates how professional Python projects are structured.

It provides practical experience with:

Modular programming

Virtual environments

Custom package creation

Dependency management

Logging

Clean project organization

These concepts are essential for real-world Python development.

Author
Maryam Fatima
