# take input of two numbers and print all the numbers between them.
number_one = (input ("Enter First Number = "))
number_two = (input("Enter Second Number = "))
if number_one != number_two:
    if number_one < number_two:
        while number_one <= number_two:
            print(number_one)
            number_one = number_one + 1
    else:
        while number_two <= number_one:
            print(number_two)
            number_two = number_two + 1
else:
    print("Please give range")