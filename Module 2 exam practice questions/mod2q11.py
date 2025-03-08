# Write a reverse number programme
number = int (input ("Enter a number which you want to make REVERSE NUMBER "))
reversenumber = 0
while number != 0:
    b = number % 10
    reversenumber = (reversenumber * 10) + b
    number = number // 10
print (reversenumber) # issue is how to remove zero?