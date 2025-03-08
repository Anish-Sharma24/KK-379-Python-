# Take input of two numbers and print all even numbers between them
no_1 = int (input ("Enter the 1st number = "))
no_2 = int (input ("Enter the 2nd number = "))
if no_1 < no_2:
    while no_1 <= no_2:
        if no_1 % 2 == 0:
            print (no_1)
        no_1 = no_1 + 1
else:
    while no_2 <= no_1:
        if no_2 % 2 == 0:
            print (no_2)
        no_2 = no_2 + 1