# Python Continue Statement in While Loop example
i = 0
while(i <= 10):
    if (i== 5 or i == 9):
        print("Skipped Values =  ", i)
        i = i + 1
        continue
    print(" The Value of the Variable i is:  ", i)
    i = i + 1

