a = int (input ("1st Number = "))
b = int (input ("2nd Number = "))
if a < b:
    for x in range (a, b, 1):
        if a % 2 == 0:
            print (a,"even number")
        else:
            print (a,"odd number")
else:
    for x in range (b, a, 1):
        if b % 2 == 0:
            print (x,"even number")
        else:
            print (x,"odd number")