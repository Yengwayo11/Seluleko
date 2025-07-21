#
for x in range(1,10001):
    divisor = 0
    for i in range(1,x):
        if x%i == 0:
            divisor += i
    if divisor == x:
        print(x)