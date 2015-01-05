class Employee:
	empCount = 0

	def __init__(self,name,sex):
		self.name = name
		self.sex = sex
		Employee.empCount += 1
	
	def displayCount(self):
		print "Total Employee",Employee.empCount
	
	def displayEmployee(self):
		print "Name: ",self.name,"\nSex: ",self.sex

flag = "y"

while flag == "y" or flag == "Y":
	name = raw_input("please enter a name:\n")
	sex = raw_input("please enter sex:")
	emp = Employee(name,sex);
	print "Ok! last employee information as follow\n"
	emp.displayEmployee()
	flag = raw_input("if u want continue,please enter 'y' or 'Y' ")

else: print "Good Bye!"
