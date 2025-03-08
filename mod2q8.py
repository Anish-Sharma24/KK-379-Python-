# Print Fibonacci series upto nth number.
n = int (input ("Nth number : "))
count = 2
no1 = 0
no2 = 1
print (no1)
print (no2)
while count <= n:
    no3 = no1 + no2
    print (no3)
    no1 = no2
    no2 = no3
    count = count + 1