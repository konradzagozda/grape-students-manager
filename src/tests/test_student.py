from services import StudentService

def test_get_all_students_empty(db):
    students = StudentService.get_all_students()
    assert students == []

def test_create_and_get_student(db):
    student_data = {"name": "John", "surname": "Doe", "specialization": "Maths"}
    created_student = StudentService.create_student(student_data)

    assert created_student.id is not None
    assert created_student.name == "John"
    assert created_student.surname == "Doe"
    assert created_student.specialization == "Maths"

    fetched_student = StudentService.get_student_by_id(created_student.id)
    
    assert fetched_student.id == created_student.id
    assert fetched_student.name == created_student.name
    assert fetched_student.surname == created_student.surname
    assert fetched_student.specialization == created_student.specialization

def test_update_student(db):
    student_data = {"name": "John", "surname": "Doe", "specialization": "Maths"}
    created_student = StudentService.create_student(student_data)
    
    update_data = {"name": "Jane", "surname": "Doe", "specialization": "Physics"}
    updated_student = StudentService.update_student(created_student.id, update_data)

    assert updated_student.id == created_student.id
    assert updated_student.name == "Jane"
    assert updated_student.surname == "Doe"
    assert updated_student.specialization == "Physics"

def test_delete_student(db):
    student_data = {"name": "John", "surname": "Doe", "specialization": "Maths"}
    created_student = StudentService.create_student(student_data)
    
    deleted_student = StudentService.delete_student(created_student.id)

    assert deleted_student is not None
    assert deleted_student.id == created_student.id

    deleted_student_again = StudentService.delete_student(created_student.id)

    assert deleted_student_again is None