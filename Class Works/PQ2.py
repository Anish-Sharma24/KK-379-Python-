# Take input of two numbers and if the second number is bigger then print from smallet number to highest number
number_1 = int (input ("Enter the First number = "))
number_2 = int (input ("Enter the Second number = "))
if number_2 > number_1:
    while number_2 >= number_1:
        print (number_1)
        number_1 = number_1 + 1
else:
    reserve = number_1
    number_1 = number_2
    number_2 = reserve
    while number_2 >= number_1:
        print (number_1)
        number_1 = number_1 + 1
