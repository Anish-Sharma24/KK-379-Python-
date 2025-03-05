# input number is Prime or not Prime
n = int (input ("Enter the to check whether is it Prime or not = "))
c = 2
#count = 0
bc = 0
while c < n - 1:
    if n % c == 0:
        bc = 0
        break
    else:
        bc = bc + 1
    c = c + 1
if bc == 0:
    print ("[",n,"] is not a Prime number")
elif bc != 0:
    print ("[",n,"] is a Prime number")