addition=123 #global variable
def Adding(a, b):
    Sum = a + b #local variable Sum
    print(addition)
    print(Sum)
def sub(a, b):
    sub = a - b #local variable Sum
    print(addition)
    return sub
def message():#default function
    print("am from default function")
def message1():#default function
    return "am from function"
Adding(3, 4)
msg=message1()
print(msg)
print(message1())
print("After Calling the sub Function:",sub(3, 4))
message()
