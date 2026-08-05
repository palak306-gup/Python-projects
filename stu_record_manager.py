# Simple Student Records Manager

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, grade):
        self.students[student_id] = {"name": name, "grade": grade}
        print(f"Added student: {name}")

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return
        
        print("\n--- Student Database ---")
        for sid, info in self.students.items():
            print(f"ID: {sid} | Name: {info['name']} | Grade: {info['grade']}")

if __name__ == "__main__":
    db = StudentManager()
    db.add_student("S101", "Palak", "A")
    db.add_student("S102", "Nishank", "B+")
    db.display_students()
