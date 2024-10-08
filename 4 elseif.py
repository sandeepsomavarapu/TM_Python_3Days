# Example for Python Elif Statement

# Imagine you have 6 subjects and Grand total is 600
Totalmarks = int(input(" Please Enter Your Total Marks:  "))
if Totalmarks >= 540:
    print(" Congratulations! ")
    print(" You are eligible for Full Scholarship ")
elif Totalmarks >= 480:
    print(" Congratulations! ")
    print(" You are eligible for 50 Percent Scholarship ")
elif Totalmarks >= 400:
    print(" Congratulations! ")
    print(" You are eligible for 10 Percent Scholarship ")
else:
    print(" You are Not eligible for Scholarship ")
    print(" We are really Sorry for You ")
