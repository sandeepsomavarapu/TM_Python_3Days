class Student:
	id=10
	name="hello"
	def __init__(self,sid):#one param-constructor #last constructor will be considered when we have many
		self.id=sid
	def __init__(self,id,name):#two param-sconstructor
		self.id=id
		self.name=name
	def add(self,a,b):
		res=a+b
		print("sum of two numbers is : ",res)
s=Student(30,'suresh')#calling ()
print(s.id)
print(s.name)
s.add(20,30)
s1=Student(20,'mahesh')#
print(s1.id)
print(s1.name)
	