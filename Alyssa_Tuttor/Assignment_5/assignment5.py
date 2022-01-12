"""
Assignment 5 for UNC_______
This assignment will read a text file of students to calculate their grades and 
produce the results to an output file.
@Author: ____________
@source
"""
# import statements used in program #
import os.path
import sys


# https://www.pythontutorial.net/python-basics/python-read-text-file/ #
# https://www.pythontutorial.net/python-basics/python-check-if-file-exists/ #
# changed name of sample_grade_input.txt to input.txt to make testing faster #
def readFile():
	# empty list to hold student info #
	students =[]
	exist = False
	
	# read file to a str object called content loop if file does not exist #
	while(exist == False):
		fileName = input(" Enter a file name!, File must be in the same folder. ")
		exist = os.path.exists(fileName)
		if(exist == True):
			f = open(fileName,'r')
			content = f.read()

	# split the list of students by "\n"(new line) to get rid of \n in list #
			students = content.split("\n")
			f.close()
			return students
		
		if(exist == False):
			print(" File name does not exist try agian ")

def writeFile(a_list):
	length = len(a_list)
	fileName = input(' Enter a filename for export ')
	f = open(fileName,'w')
	for i in range(length):
		f.write(a_list[i])
		f.write('\n')
	f.close()

def gradeGRAD(x):
	letter = 'X'
	if( x >= 95):
		letter = 'H'
	elif( x >= 80 and x <= 94):
		letter = 'P'
	elif( x >= 70 and x<= 79):
		letter = 'L'
	elif( x >= 0 and x<= 69):
		letter = 'F'
	else:
		print(' FILE ERROR: check GRAD number grade! ')
		sys.exit()
	return letter

def gradeUNDERGRAD(x):
	letter = 'X'
	if( x >= 90):
		letter = 'A'
	elif( x >= 80 and x <= 89):
		letter = 'B'
	elif( x >= 70 and x<= 79):
		letter = 'C'
	elif( x >= 60 and x<= 69):
		letter = 'D'
	elif( x >= 0 and x<= 59):
		letter = 'F'
	else:
		print(' FILE ERROR: check UNDERGRAD number grade! ')
		sys.exit()
	return letter

# the grading function to run the assignment algorithim #
def gradeStudents(a_list):
	# set up variables to use #
	grad = False
	counter = 1
	data = 0
	output = []
	length = len(a_list)
	# loop through the list counting each line as you move #
	# one student involves 3 data lines this means loop runs 3 times per student #
	for i in range(length):
		data = a_list[i]
		if(counter == 1):
			if(data == 'GRAD'):
				grad = True
			elif(data == 'UNDERGRAD'):
				grad = False
			else:
				print(' FILE ERROR: check GRAD and UNDERGRAD values! ')
				sys.exit()
		elif(counter == 2):
			output.append(data)
		elif(counter == 3):
			if(grad == True):
				output.append(gradeGRAD(int(data)))
			else:
				output.append(gradeUNDERGRAD(int(data)))
			counter = 0
		counter += 1
	return output

def curveList(a_list):
	x = input(' Enter a value to be the new 100%: ')
	data = 0
	counter = 1
	length = len(a_list)
	for i in range(length):
		# do nothing for counter at 1 #
		# counter at 2 will run the grade curve algorithim #
		if(counter == 3):
			data = curve(int(a_list[i]),int(x))
			a_list[i] = data
			counter = 0
		counter += 1
	return a_list

# x = value to relate to y, y = the new 100% #
def curve(x,y):
	z = 0
	if( x == y):
		x = 100
	elif(x < y):
		z = y / x
		x = 100 / z
	elif(x > y):
		z = x/y
		x = 100 * z
	return x

# https://www.w3schools.com/python/python_ref_list.asp #
# will clean the list of any unnesarry blank space #
def cleanData(a_list):
	count = a_list.count('')
	while count != 0:
		a_list.remove('')
		count -= 1 

# main running part of the program will call and run functions #
def main():
	students = readFile()
	cleanData(students)
	value = input(' Do you want to grade on a curve?(y/n): ')
	if(value == 'n'):
		output = gradeStudents(students)
		writeFile(output)
		#print(students)
		#print(output)
	elif(value == 'y'):
		students = curveList(students)
		output = gradeStudents(students)
		writeFile(output)
		#print(students)
		#print(output)
	else:
		print(' INPUT ERROR: invalid y/n input try lower case no spaces! ')

# command to run the main function #
main()
