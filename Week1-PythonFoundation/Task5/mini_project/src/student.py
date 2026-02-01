class Student:
    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department
        }
