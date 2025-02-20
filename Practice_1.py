# take input of two numbers and print all the odd numbers and even numbers between them.
a = int (input ("Enter First Number (a) = "))
b = int (input("Enter Second Number (b) = "))
if a < b:
    while a <= b:
        if a % 2 == 0:
            print (a,"Even number")
        elif a % 2 == 1:
            print ("Odd number",a)
        a = a + 1
else:
    while b <= a:
        if b % 2 == 0:
            print (b, "Even number")
        elif b % 2 == 1:
            print ("Odd number",b)
        b = b + 1