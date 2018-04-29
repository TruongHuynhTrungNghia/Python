#! /usr/bin/python3

class Student:
	students=[]
	def __init__(self,name,department):
		self.name=name
		self.department=department

	def input(self,numberOfStudent=0):
		for i in range(int(numberOfStudent)):
			sName=input("Student name: ")
			sDep=input("Department: ")
			Student.students.append(Student(sName,sDep))

	def output(self):
		for student in Student.students:
			print(student.name+ " is in "+student.department)

	def sort(self):
		Student.students=sorted(Student.students,key =lambda student:student.name)
	
