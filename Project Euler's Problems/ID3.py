# Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
mainloop = 2
subloop = 2
largest = 0
while mainloop <= 600851475143:
    if 600851475143 % mainloop == 0:
        while subloop <= mainloop - 1:
            if mainloop % subloop == 0:
                break
            subloop = subloop + 1
    mainloop = mainloop + 1
