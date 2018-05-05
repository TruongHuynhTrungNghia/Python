#! /usr/bin/python3

from undergraduate import Undergraduate
from graduate import Graduate

students = []
graduate_stus = []

def represents_int(str ):
	try: 
		int(str )
		return True
	except ValueError:
		return False

number_of_student = input("Number Of Student: ")
while represents_int(number_of_student) == False or 
	  int(number_of_student)<0:
	print("You suppose to input an integer. Please input againt")
	number_of_student = input("Number Of Student: ")
	if represents_int(number_of_student) and 
	    int(number_of_student)>0:		
			break

#insert student to the list students
for i in range(int(number_of_student)):
	print("student {}".format(i+1))
	stu_name = input("Student name: ")
	stu_dep = input("Department: ")
	check_graduate = input("graduated ?[y/n]")
	if check_graduate == 'y':
		company_name = input("company name: ")
		graduate_stus.append(Graduate(stu_name,stu_dep,company_name))
	elif check_graduate == 'n':
		stu_ID = input("Student ID: ")
		students.append(Undergraduate(stu_name,stu_dep,stu_ID))

#sort student's name in the list in accending order
for student in students:
	students = sorted(students, key =lambda student:student.name)
for student in graduate_stus:
	graduate_stus = sorted(graduate_stus, key =lambda student:student.name)

#printing...
print("print...")

#print list of undergraduated student
print("")
print("undergraduated student:  ")
for student in students:
	print("")
	print(student.get_undergra_stu_info())

#print list of graduated student print("") print("graduated student:  ") for
student in graduate_stus:    
	print(" ")
	print(student.get_graduate_stu_info())


