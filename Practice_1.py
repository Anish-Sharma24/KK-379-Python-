# take input of two numbers and print all the numbers between them.
a = (input ("Enter First Number = "))
b = (input("Enter Second Number = "))
if a != b:
    if a < b:
        while a <= b:
            print(a)
            a = a + 1
    else:
        while b <= a:
            print(b)
            b = b + 1
else:
    print("Please give range")