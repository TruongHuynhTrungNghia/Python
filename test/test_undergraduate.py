#test_graduated.py


import pytest
import sys


from product.undergraduate import Undergraduated

def test_graduated_student_1():
	test = Undergraduated("Nghia", "is", "123")
	assert test.get_undergra_stu_info() == "name: Nghia" + "\ndepartment: is" + "\nstudent ID: 123"

def test_graduated_student_2():
	test = Undergraduated("", "", "")
	assert test.get_undergra_stu_info() == "name: " + "\ndepartment: " + "\nstudent ID: "

def test_graduated_student_3():
	test = Undergraduated()
	assert test.get_undergra_stu_info() == "name: " + "\ndepartment: " + "\nstudent ID: "

def test_graduated_student_4():
	test = Undergraduated("nghia")
	assert test.get_undergra_stu_info() == "name: nghia" + "\ndepartment: " + "\nstudent ID: "

def test_graduated_student_5():
	test = Undergraduated("nghia","is",)
	assert test.get_undergra_stu_info() == "name: nghia" + "\ndepartment: is" + "\nstudent ID: "

#error!!!
# def test_graduated_student_6():
# 	test = Graduated(, "is", "abc")
# 	assert test.get_graduate_stu_info() == "name: " + "\ndepartment: is" + "\ncompany: ktm"
