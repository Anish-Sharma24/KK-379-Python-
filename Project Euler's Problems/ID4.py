# Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99
# Find the largest palindrome made from the product of two 3-digit numbers.
loop1 = 100
loop2 = 100
number = 0
q = 0
reversenumber = 0
while loop1 < 1000:
    while loop2 < 1000:
        number = loop1 * loop2
        while number != 0:
            q = number % 10
            reversenumber = (reversenumber * 10) + q
            number = number // 10
        loop2 = loop2 + 1
        if reversenumber == number:
            print (reversenumber)
    loop1 = loop1 + 1