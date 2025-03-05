n1 = 2
while n1 < 100:
    c = 2
    count = 0
    breakcount = 0
    while c <= n1 - 1:
        if n1 % c == 0:
            breakcount = breakcount + 1
            break
        elif n1 % c != 0:
            count = count + 1
        c = c + 1
    if breakcount == 0:
        print (n1)
    n1 = n1 + 1