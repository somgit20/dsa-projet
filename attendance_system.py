# attendance_system.py
from collections import deque

class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.attendance_count = 0

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Attendance: {self.attendance_count}"


class AttendanceSystem:
    def __init__(self):
        # dictionary to store students keyed by ID
        self.students = {}
        # queue to track the order of marked attendance
        self.attendance_queue = deque()

    def add_student(self, student_id, name):
        """Add a new student. Returns True if added, False if ID exists."""
        if student_id in self.students:
            return False
        self.students[student_id] = Student(student_id, name)
        return True

    def mark_attendance(self, student_id):
        """Mark attendance for the given student ID. Returns True on success."""
        if student_id in self.students:
            student = self.students[student_id]
            student.attendance_count += 1
            self.attendance_queue.append(student_id)
            return True
        return False

    def get_all_students(self):
        """Return a list of Student objects."""
        return list(self.students.values())

    def search_student(self, student_id):
        """Return Student object or None if not found."""
        return self.students.get(student_id)

    def get_attendance_order(self):
        """Return Student objects in the order attendance was marked."""
        return [self.students[sid] for sid in self.attendance_queue if sid in self.students]
