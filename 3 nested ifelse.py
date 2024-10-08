age = int(input(" Please Enter Your Age Here:  "))
if age < 18:
    print(" You are Minor ") 
    print(" You are not Eligible to Work ") 
else:
    if age >= 18 and age <= 60:
        print(" You are Eligible to Work ")
        print(" Please fill in your details and apply")
    else:
        print(" You are too old to work as per the Government rules")
        print(" Please Collect your pension!")
