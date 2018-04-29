#! /usr/bin/python3

from student import Student

def main():
	numberOfStudent=input("Number Of Student: ")
	stu=Student("",0)
	stu.input(numberOfStudent)
	stu.output()
if __name__ == '__main__':
	main()
