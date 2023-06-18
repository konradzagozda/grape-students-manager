import requests

BASE_URL = 'http://localhost:5000/api/v1/students'


def test_get_all_students():
    response = requests.get(BASE_URL + '/')
    assert response.status_code == 200

def test_create_and_get_student():
    student_data = {"name": "John", "surname": "Doe", "specialization": "Maths"}
    post_response = requests.post(BASE_URL + '/', json=student_data)
    assert post_response.status_code == 201
    created_student = post_response.json()

    get_response = requests.get(BASE_URL + '/' + created_student['id'])
    assert get_response.status_code == 200
    fetched_student = get_response.json()

    assert fetched_student['id'] == created_student['id']
    assert fetched_student['name'] == created_student['name']
    assert fetched_student['surname'] == created_student['surname']
    assert fetched_student['specialization'] == created_student['specialization']

def test_update_student():
    student_data = {"name": "Jane", "surname": "Doe", "specialization": "Physics"}
    post_response = requests.post(BASE_URL + '/', json=student_data)
    assert post_response.status_code == 201
    created_student = post_response.json()

    update_data = {"name": "John", "surname": "Doe", "specialization": "Maths"}
    put_response = requests.put(BASE_URL + '/' + created_student['id'], json=update_data)
    assert put_response.status_code == 200
    updated_student = put_response.json()

    assert updated_student['id'] == created_student['id']
    assert updated_student['name'] == "John"
    assert updated_student['surname'] == "Doe"
    assert updated_student['specialization'] == "Maths"

def test_delete_student():
    student_data = {"name": "John", "surname": "Doe", "specialization": "Maths"}
    post_response = requests.post(BASE_URL + '/', json=student_data)
    assert post_response.status_code == 201
    created_student = post_response.json()

    delete_response = requests.delete(BASE_URL + '/' + created_student['id'])
    assert delete_response.status_code == 200

    get_response = requests.get(BASE_URL + '/' + created_student['id'])
    assert get_response.status_code == 404