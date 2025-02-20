# Input two numbers and print all the numbers between them.
no1 = int (input ("Enter the 1st number = "))
no2 = int (input ("Enter the 2nd number = "))
if no1 < no2:
    while no1 < no2:
        no1 = no1 + 1
        if no1 == no2:
            continue
        else:
            print (no1)
else:
    while no2 < no1:
        no2 = no2 + 1
        if no2 == no1:
            continue
        else:
            print (no2)