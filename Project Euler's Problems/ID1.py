# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#n1 = int (input ("Input upto : "))
sum3 = 0
sum5 = 0
loop = 1
count = 0
while loop < 1000:
    if loop % 3 == 0:
        sum3 = sum3 + loop
        print (loop)
    if loop % 5 == 0:
        sum5 = sum5 + loop
        print (loop)
    loop = loop + 1
print ("Total of multiple of 3 ", sum3)
print ("Total of multiple of 5", sum5)
print ("Sum of both multiple of 3 and 5 is ",sum3 + sum5)