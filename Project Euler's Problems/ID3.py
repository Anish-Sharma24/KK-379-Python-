# Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
mainloop = 2
basicstore = 0
largerstore = 0
count = 0
number = int (input ("Enter the number = "))
while mainloop < number:
    if number % mainloop == 0:
        subloop = 2
        while subloop < mainloop:
            if mainloop % subloop == 0:
                count = 1
                break
            else:
                count = 0
            if mainloop > basicstore:
                basicstore = mainloop
            subloop = subloop + 1
        if count == 0:
            print (mainloop)
    mainloop = mainloop + 1