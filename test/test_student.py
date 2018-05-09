#test_student.py

import pytest
#import sys

#sys.path.insert(0, '..')

from product.student import Student


def test_student_1():
	test = Student("Nghia", "is")
	assert test.get_stu_info() == "name: Nghia" + "\ndepartment: is"

def test_student_2():
	test = Student("", "")
	assert test.get_stu_info() == "name: " + "\ndepartment: "

def test_student_3():
	test = Student()
	assert test.get_stu_info() == "name: " + "\ndepartment: "

def test_student_4():
	test = Student("nghia")
	assert test.get_stu_info() == "name: nghia" + "\ndepartment: "

#error!!!
# def test_student_5():
# 	test = Student(,"is")
# 	assert test.get_stu_info() == "name: " + "\ndepartment: is"