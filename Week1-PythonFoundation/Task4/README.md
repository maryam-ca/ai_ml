📌 Task 4 – Python Libraries & Packaging
📖 Overview

This task focuses on learning how to write clean, modular, and production-ready Python code.
The project demonstrates how to organize Python programs using modules, virtual environments, and custom packages, along with logging and proper documentation.

This task helps in understanding how real-world Python projects are structured and managed.

✨ Features
🔹 Modular Programming

Python code is divided into multiple modules.

Each module has a single responsibility.

Modules are reused using proper import statements.

🔹 Virtual Environment

A virtual environment (venv) is created to isolate the project.

Prevents conflicts between project dependencies.

Ensures clean and safe package management.

🔹 Custom Python Package

A custom package named mypackage is created.

Proper folder structure is followed.

__init__.py is used to expose package functions.

Package is installed locally using pip install .

🔹 Logging

Python’s built-in logging module is used.

Logs are stored in a file instead of using print.

Makes the project more production-ready.

🔹 Clean Project Structure

Logical folder organization.

Separate folders for modules, package, and tests.

Easy to read, maintain, and extend.

📁 Project Structure
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

▶️ How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv

2️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate


After activation, (venv) will appear in the terminal.

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Custom Package

Navigate to the mypackage folder:

cd mypackage
pip install .

5️⃣ Run Test Files

Go back to Task4 folder:

cd ..
python test_package.py

✅ Expected Output
20
nohtyp

🧪 Testing

test_modules.py tests modular scripts.

test_package.py tests the custom Python package.

Successful output confirms correct installation and imports.

🧑‍💻 Author

Maryam Fatima
