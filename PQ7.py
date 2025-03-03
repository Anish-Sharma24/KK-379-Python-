# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 100.
print ("Must enter a range")
n1 = int (input ("Enter 1st number of the range = "))
n2 = int (input ("Enter 2nd number of the range = "))
sum3 = 0
sum5 = 0
bothsum = 0
count3 = 0
count5 = 0
bothcount = 0
if n1 < n2:
    while n1 <= n2:
        if n1 % 3 == 0 and n1 % 5 == 0:
            bothsum = bothsum + n1
            bothcount = bothcount + 1
        elif n1 % 3 == 0:
            sum3 = sum3 + n1
            count3 = count3 + 1
        elif n1 % 5 == 0:
            sum5 = sum5 + n1
            count5 = count5 + 1
        n1 = n1 + 1
    print ("The sum of all 3's and 5's multiples is [", bothsum + sum3 + sum5,"]")
    print ("Total [", bothcount,"] natural numbers which are multiple of both 3 and 5")
    print ("Total [", count3,"] natural numbers which are multiple of 3")
    print ("Total [", count5,"] natural numbers which are multiple of 5")
elif n2 < n1:
    while n2 <= n1:
        if n2 % 3 == 0 and n2 % 5 == 0:
            bothsum = bothsum + n1
            bothcount = bothcount + 1
        elif n2 % 3 == 0:
            sum3 = sum3 + n1
            count3 = count3 + 1
        elif n2 % 5 == 0:
            sum5 = sum5 + n1
            count5 = count5 + 1
        n2 = n2 + 1
    print ("The sum of all 3's and 5's multiples is [", bothsum + sum3 + sum5,"]")
    print ("Total [", bothcount,"] natural numbers which are multiple of both 3 and 5")
    print ("Total [", count3,"] natural numbers which are multiple of 3")
    print ("Total [", count5,"] natural numbers which are multiple of 5")
else:
    print ("Both the inputs are same. Please provide a range")