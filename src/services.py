
from models import Student
from models import db

class StudentService:
    @staticmethod
    def get_all_students(name=None, surname=None, specialization=None):
        query = Student.query
        if name:
            query = query.filter_by(name=name)
        if surname:
            query = query.filter_by(surname=surname)
        if specialization:
            query = query.filter_by(specialization=specialization)
        return query.all()

    @staticmethod
    def create_student(payload):
        new_student = Student(**payload)
        db.session.add(new_student)
        db.session.commit()
        return new_student

    @staticmethod
    def get_student_by_id(id):
        return Student.query.filter(Student.id == id).first_or_404()

    @staticmethod
    def update_student(id, new_student):
        student = StudentService.get_student_by_id(id)
        student.name = new_student["name"]
        student.surname = new_student["surname"]
        student.specialization = new_student["specialization"]
        db.session.commit()
        return student

    @staticmethod
    def delete_student(id):
        student = Student.query.filter(Student.id == id).first()
        if student:
            db.session.delete(student)
            db.session.commit()
        return student