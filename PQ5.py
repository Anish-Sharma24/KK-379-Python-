# Input two numbers and print all prime numbers between them

print (" The First input always should be >1 as no. 1 is not a prime number")
n1 = int (input ("Please enter the 1st number = "))
n2 = int (input ("Please enter the 2nd number = "))
if n1 < n2:
    if n1 == 1:
        n1 = n1 + 1
    while n1 < n2:
        c = 2
        count = 0
        breakcount = 0
        while c <= n1 - 1:
            if n1 % c == 0:
                breakcount = breakcount + 1
                break
            elif n1 % c != 0:
                count = count +1
            c = c + 1
        if breakcount == 0:
            print (n1)    
        n1 = n1 + 1
elif n2 < n1:
    if n2 == 1:
        n2 = n2 + 1
    while n2 <= n1:
        c = 2
        count = 0
        breakcount = 0
        while c <= n2 - 1:
            if n2 % c == 0:
                breakcount = breakcount + 1
                break
            elif n2 % c != 0:
                count = count + 1
            c = c + 1
        if breakcount == 0:
            print (n2)
        n2 = n2 + 1
else:
    print ("Both the inputs are same please provide a range to calculate Prime numbers")