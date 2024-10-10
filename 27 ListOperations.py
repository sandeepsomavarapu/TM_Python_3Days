# listval=list(range(2,100,2))
names=['mahesh','naresh','mahi','rajesh','somesh','mahesh','hitesh','mahi','deep']
names1=['sunny','bunny','munny']
# result=names1*3
# print(names)
names.clear()
# print(names)
# print(result)
print(names.index('mahi'))
print(names)
names.extend(names1)
print(names)
names.remove('naresh')
names.pop()#remove the last value from list
names.pop(3)
print(names)
# names.append('excelr')#will add value  at the end 
# names.insert(1,'excelr hyd')#will add value at the specified position
# print(names)
# print(type(names))
# print(names[0:2])
# print(names.count('mahesh'))
# print('**********using while loop********')
# i=0
# print(len(names))
# while i<len(names):
#     print(names[i])
#     i=i+1  
# print('**********using for loop**********')
# for x in names:
#     if len(x)<6:
#         print(x)
# print(names)
names.reverse()
# print(names)
# names.sort(reverse=False)#by default =false ascending order 
# print(names)
# # #nested list
# nestedlist=[12,13,[1,2]]
# print(nestedlist)
# print(nestedlist[0])
# print(nestedlist[2][0])
# print(nestedlist[2][1])

numbers=[[10,20,30],[40,50,60],[70,80,90]]#-->3
# for r in numbers:
#     print(r)
for i in range(len(numbers)):#0,1,2
    for j in range(len(numbers[i])):#0,1,2
        print(numbers[i][j],end=' ')
    print()
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)  
print(lst)
