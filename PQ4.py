# Take input of two numbers and print all the odd number between them
n1 = int (input ("Insert the first number = "))
n2 = int (input ("Insert the second number = "))
if n1 < n2:
    while n1 <= n2:
        if n1 % 2 == 1:
            print (n1)
        n1 = n1 + 1
else:
    while n2 <= n1:
        if n2 % 2 == 1:
            print(n2)
        n2 = n2 + 1