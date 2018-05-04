#! /usr/bin/python3


from student import Student
class Undergraduate(Student):

	def __init__(self, name, department, stu_ID):
		Student.__init__(self,name,department)
		self.stu_ID = stu_ID

	def get_undergra_stu_info(self):
		return (self.get_stu_info() +
		"\nstudent ID: " + self.stu_ID)
