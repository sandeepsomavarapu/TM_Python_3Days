# Python Continue Statement in For Loop example

number = int(input(" Please Enter any integer Value: "))
for i in range (1, number):
    if(i%2 != 0):
        print(" Odd Numbers = {0}(Skipped By Continue)".format(i))
        continue
    print(" Even numbers = ", i)

