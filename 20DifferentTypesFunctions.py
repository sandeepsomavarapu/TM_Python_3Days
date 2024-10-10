def sayHello():#defining function using def
    print("Hello! How r  u..")
sayHello()# calling default function


def sayHi(name):#function with parameter
    print("Hello!"+ name+" How r  u..")
sayHi("sandeep") # calling param_function argument

def squareIt(number):
    print("square of  given number :",(number*number))
squareIt(2)
squareIt(12)


def cubeIt(number):
    return number*number,number*2
print(cubeIt(9))   
print(cubeIt(29))   

def Check_EvenOdd(num):
  if (num % 2 == 0):
    print(num," is EVEN")
  else:
    print(num," is ODD")
Check_EvenOdd(9)
Check_EvenOdd(12)

#arguments / parameters

def add(a,b):
    return a+b
print(add(122,121))

#Keyword arguments
def printMsg(name,msg):
    print("Hello Mr :",name,msg)
    
printMsg("suresh","very good morning")
printMsg("mahesh",msg="very good Aternoon")#valid
printMsg(msg="very good evening",name="rajesh")

#default arguments
def message(msg,name="accenture"):
    print("Hello Mr :",name,msg)

message("good afternoon","capgemini")
message("good morning")

#   variable length arguments  *

def add_fun(*number):#5,6,7
    total=0#5,11,18
    for i in number:
        total=total+i
    print("the sum of all numbers is : ",total)

add_fun()
add_fun(1,2)
add_fun(5,6,7)
add_fun(90,78,34,23)
#keyword and length by using **
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rn=123,name="sandeep",marks=230,subject="python")

#·	Unpacking Argument Lists ( unknown number of parameters )

def fun(a,b,c,d):
    print(a,b,c,d)

numbers=[22,23,23,25]

fun(*numbers)

def my_fun1():
    pass

my_fun1()

a=20 # global variable

def my_fun2():
    b=20 #local variable
    return a
def my_fun3():
    return a+3