# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#n1 = int (input ("Input upto : "))
summation = 0
loop = 1
count = 0
while loop < 1000:
    if loop % 3 == 0 or loop % 5 == 0:
       summation = summation + loop
       count = count + 1
       print (loop)
    loop = loop + 1
print ("Total is", summation)
print ("Total number multiples are ",count)