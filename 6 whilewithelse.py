# Example for While Loop with Else Statement

total = 0
number = int(input(" Please Enter any integer below 10:  "))
while (number <= 10):
    total = total + number
    number = number + 1
    print(" Value of Total From the While Loop is: ", total)
else:
    print(" You Value is Greater Than 10 ==> This is from Else Block ")
