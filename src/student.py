class Student:
    def __init__(self, student_id, name, age, department):
        if not student_id or not name or not department:
            raise ValueError("Student ID, Name and Department are required")

        if age <= 0:
            raise ValueError("Age must be a positive number")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.age = int(age)
        self.department = department.strip()

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department
        }

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.age} | {self.department}"
