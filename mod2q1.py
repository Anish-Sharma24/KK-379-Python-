# Take two integer from user and perform ADDITION, SUBSTRACTION, MULTIPLACATION, DIVISION.
def addition (x,y):
    return (x + y)
def subtraction (x,y):
    if y > x:
        return (y - x)
    return (x - y)
def multiplication (x,y):
    return (x * y)
def division (x,y):
    return (x / y)
print ("Select operations")
print ("Addition = 1 ||","Subtraction = 2 ||","Multiplicatio = 3 ||", "Division = 4 ||")
choice = int (input ("Input your Operational choice : "))
number1 = int (input ("1st number = "))
number2 = int (input ("2nd number = "))
if choice == 1:
    print ("Addition result is ", addition (number1,number2))
elif choice == 2:
    print ("Subtraction result is", subtraction (number1,number2))
elif choice == 3:
    print ("Multiplication result is ", multiplication (number1,number2))
elif choice == 4:
    print ("Division result is ", division (number1,number2))
else:
    print ("Invalid input")