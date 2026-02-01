# Task 3 – Object-Oriented & Advanced Python

## Introduction
This task is part of **Week 1 Python assignments** and focuses on learning **Object-Oriented Programming (OOP)** and **advanced Python concepts**.  
The main purpose of this task is to help learners understand how real-world problems can be solved using classes, objects, and reusable Python components.

This task also introduces internal Python concepts such as decorators and generators, which are very important for professional Python development.

---

## Objectives of This Task
- To understand how OOP works in Python
- To learn how classes and objects are created and used
- To practice inheritance and method overriding
- To understand Python magic methods
- To learn decorators and generators
- To improve clean coding and documentation skills

---

## Topics Covered

### Object-Oriented Programming (OOP)
- Classes and Objects
- Encapsulation (protecting data)
- Inheritance (parent and child classes)
- Polymorphism (same method, different behavior)
- Magic Methods such as `__init__` and `__str__`

### Advanced Python Concepts
- Custom Decorators
- Execution Time Measurement
- Iterators and Generators
- Efficient looping using `yield`

---

## Project Folder Structure

Week 1/
└── Task 3/
├── bank_account.py
├── decorators.py
├── generators.py
└── README.md


Each file is created separately to keep the code **clean, modular, and easy to understand**.

---

## File Details

### 1. bank_account.py
This file implements a **Bank Account System** using Object-Oriented Programming.

**What this file does:**
- Creates a base class `BankAccount`
- Creates a child class `SavingsAccount`
- Implements deposit and withdraw functions
- Uses encapsulation to protect account balance
- Demonstrates inheritance and polymorphism
- Uses magic methods for object initialization and printing

**OOP Concepts Used:**
- Class and Object
- Encapsulation
- Inheritance
- Polymorphism
- Magic Methods

---

### 2. decorators.py
This file demonstrates how **decorators** work in Python.

**What this file does:**
- Creates a custom decorator
- Measures the execution time of a function
- Shows how one function can wrap another function

**Concepts Practiced:**
- Decorators
- Function wrapping
- Python function execution flow

---

### 3. generators.py
This file focuses on **generators and iterators**.

**What this file does:**
- Generates Fibonacci numbers using a generator
- Creates a custom range function
- Uses `yield` instead of `return`
- Demonstrates memory-efficient looping

**Concepts Practiced:**
- Generators
- Iterators
- Efficient memory usage

---

## How to Run the Programs

Follow the steps below to run the Python files:

1. Open Command Prompt or Terminal  
2. Navigate to the `Task 3` folder  
3. Run the following commands one by one:

```bash
python bank_account.py
python decorators.py
python generators.py
