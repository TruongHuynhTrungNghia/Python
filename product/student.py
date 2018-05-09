#! /usr/bin/python3


class Student:


	name =""
	department=""

	def __init__(self, name="", department=""):
		self.name = name
		self.department = department

	def get_stu_info(self):
		return ("name: " + self.name + 
		"\ndepartment: " + self.department)
	
	
