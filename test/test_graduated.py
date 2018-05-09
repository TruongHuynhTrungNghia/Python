#test_graduated.py


import pytest

from product.graduate import Graduated

def test_graduated_student_1():
	test = Graduated("Nghia", "is", "abc")
	assert test.get_graduate_stu_info() == "name: Nghia" + "\ndepartment: is" + "\ncompany: abc"

def test_graduated_student_2():
	test = Graduated("", "", "")
	assert test.get_graduate_stu_info() == "name: " + "\ndepartment: " + "\ncompany: "

def test_graduated_student_3():
	test = Graduated()
	assert test.get_graduate_stu_info() == "name: " + "\ndepartment: " + "\ncompany: "

def test_graduated_student_4():
	test = Graduated("nghia")
	assert test.get_graduate_stu_info() == "name: nghia" + "\ndepartment: " + "\ncompany: "

def test_graduated_student_5():
	test = Graduated("nghia","is",)
	assert test.get_graduate_stu_info() == "name: nghia" + "\ndepartment: is" + "\ncompany: "

#error!!!
# def test_graduated_student_6():
# 	test = Graduated(, "is", "abc")
# 	assert test.get_graduate_stu_info() == "name: " + "\ndepartment: is" + "\ncompany: ktm"
