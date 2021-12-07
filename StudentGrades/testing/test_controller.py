from StudentGrades.controller import *
from django.test import RequestFactory
from unittest.mock import patch
import pytest


factory = RequestFactory()
students = {}

def mocked_student(id):
    print('hihi')
    return students[id]
# @pytest.mark.django_db
def setup_module(module):   
    for i in range(200):
        #students[i] ={"student_name": f"Student{i}", "email": f"student{i}@example.com", "mobile_phone":"0123456789 "}
        students[i] = [Student(student_name=f"Student{i}", email=f"student{i}@example.com", mobile_phone="0123456789 ")]

#@pytest.mark.django_db
@patch("StudentGrades.controller.query_student", mocked_student)
def test_get_one_student():
    # Get student 150
    request = factory.get('/students/150') 
    print(get_one_student(request, id=150))
    # Check 
    # assert cache.head is not None
    # assert cache.head = cache.detail

    ### Check insert 1 new 
    ## Cache (hash table)
    ## Linked list
    assert cache.

# @pytest.mark.django_db
def teardown_module(module):
    # for i in range(200):
    #     student = Student.objects.get(student_name=f"Student{i}", email=f"student{i}@example.com", mobile_phone="0123456789")
    #     student.delete()
    # student = Student.objects.filter()
    pass
    