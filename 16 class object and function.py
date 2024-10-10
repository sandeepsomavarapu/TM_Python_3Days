class Employee:
    company = 'welcome to programming'
    def __init__(self, name, age, gender):
        print("param constructor")
        self.name = name
        self.age = age
        self.gender = gender	
        print('Welcome to Python Programming'+self.name)
    def __del__(self):
        print("destroyed....")  
    def func_message(self):
        print('Welcome to Python Programming'+self.name)
emp1 = Employee('Mike', 25, 'Male') #()-->constructor calling

print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
del emp1




