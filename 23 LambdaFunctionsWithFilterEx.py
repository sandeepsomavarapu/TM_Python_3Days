#with out lambda
def  getEven(x):
    if x%2==0:
        return True
    else:
        return False    
li=[23,12,56,3,9,18,4]

l1=list(filter(getEven,li))
print(l1)
# with lambda``
l2=list(filter(lambda a:a%2==0,li))
print(l2)

#list of names  below 6 
# =>,->,lambda
def getNames(name):
    if(len(name)<6):
        return True
    else:
        return False
l4=tuple(filter(getNames,('suresh','naresh','ramesh','rajesh','somesh','xyz','abc')))
print(l4)

l3=list(filter(lambda name:len(name)<6,['suresh','naresh','ramesh','rajesh','somesh','xyz','abc']))
print(l3)