#! /usr/bin/python3

# from product.undergraduate import Undergraduated
# from product.graduate import Graduated
from undergraduate import Undergraduated
from graduate import Graduated

students = []
graduate_stus = []

def represents_int(str ):
	try: 
		int(str )
		return True
	except ValueError:
		return False

def sort_stu(list = []):
	for student in list:
		list = sorted(list, key =lambda student:student.name)
	return list

def insert_student():
	number_of_student = input("Number Of Student: ")
	while represents_int(number_of_student) == False or int(number_of_student)<0:
		print("You suppose to input an integer. Please input againt")
		number_of_student = input("Number Of Student: ")
		if represents_int(number_of_student) and int(number_of_student)>0:		
			break
	#insert student to the list students
	for i in range(int(number_of_student)):
		print("student {}".format(i+1))
		stu_name = input("Student name: ")
		stu_dep = input("Department: ")
		check_graduate = input("graduated ?[y/n]")
		if check_graduate == 'y':
			company_name = input("company name: ")
			graduate_stus.append(Graduated(stu_name,stu_dep,company_name))
		elif check_graduate == 'n':
			stu_ID = input("Student ID: ")
			students.append(Undergraduated(stu_name,stu_dep,stu_ID))

def output():
	print("")
	print("undergraduated student:  ")
	for student in students:
		print("")
		print(student.get_undergra_stu_info())
	print("")
	print("graduated student: ")
	for student in graduate_stus:   
		print(" ")
		print(student.get_graduate_stu_info())

def main():
	insert_student()
	global students
	global graduate_stus
	if students != "":
		students = sort_stu(students)
	if graduate_stus != "":
		graduate_stus = sort_stu(graduate_stus)
	output()

if __name__ == '__main__':
	main()