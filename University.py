#! /usr/bin/python3

from student import Student

students=[]
def main():
	numberOfStudent=input("Number Of Student: ")
	while RepresentsInt(numberOfStudent)==False or int(numberOfStudent)<0:
		print("You suppose to input an integer. Please input againt")
		numberOfStudent=input("Number Of Student: ")
		if RepresentsInt(numberOfStudent) and int(numberOfStudent)>0:
			break
	stu=Student("","")
	stu.input(numberOfStudent)
	stu.sort()
	stu.output()
	

def RepresentsInt(str):
	try: 
		int(str)
		return True
	except ValueError:
		return False

if __name__ == '__main__':
	main()