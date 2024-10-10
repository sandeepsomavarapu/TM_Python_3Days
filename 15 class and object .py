class Employee:
	company =None#if there is no static keyword then it is instance var
	a=123
	def func_message(self,company):#self indicates current class object
		self.company=company
		print('Welcome to Python Programming')
	def  addition(self,x,y):
		res=x+y
		print(res)
	def __init__(self):# default constructor
		print(self,"@constructor")
		print('am from default contructor .....')	
emp1 = Employee() # Created an Instance   CAR ,TREE
print(emp1,"@ line 14")
print(emp1.company)
emp1.func_message("accenture")
print(emp1.company)
emp1.addition(123,234)
