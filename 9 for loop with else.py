# Python For Loop Else statement Example

number = int(input(" Please Enter any integer below 100:  "))

for i in range(0, 100):
    if number == i:
        print(" User entered Value is within the Range (Below 100)")
        break
else:
    print(" User entered Value is Outside the Range (Above 100)")

