# students={}
# students[100]='mahesh'
# students[200]='rajesh'
# students[300]='suresh'
# print(students)
# print(students[100])
# employees={111:'bunny',222:'sunny',333:'munny'}
# print(employees)
# print(employees[111])
# print(employees.keys())
# print(employees.values())
# del employees[222]
# print(employees)
# #employees.clear()
# print(len(employees))

# print(employees.popitem())
# print(employees)
# print(employees.get(333))
# print(employees.pop(111))
# #print(employees.popitem())
# print(employees)
employees1={111:'bunny',222:'sunny',333:'munny'}

result=employees1.items()
print(len(result))
for item in result:
    print(item)
