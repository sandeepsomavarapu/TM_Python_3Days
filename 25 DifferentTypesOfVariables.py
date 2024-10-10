class Employee:
    def __init__(self):
        Employee.orgName="Excelr"
        self.empno=100  #instance variable declaration inside the constructor using self keyword
    def empInfo(self):
        marks=123#local variable
        Employee.countryName="india"
        self.empName="abhay"#instance variable declaration inside the function using self keyword
emp=Employee()
emp.empInfo()
emp.empSal=23000 #instance variable declaration outside the class using obj reference
print(emp.empno,":",emp.empName,":",emp.empSal)
print(Employee.orgName,":",Employee.countryName)