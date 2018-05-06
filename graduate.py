#! /usr/bin/python3

from student import stu

class graduated(stu):

	def __init__(self, name, department, company):
		stu.__init__(self, name, department)
		self.company = company

	def get_graduate_stu_info(self):
		return (self.get_stu_info() + 
			   "\ncompany: " + self.company)