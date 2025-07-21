#
x = n**2 - 2*n + 2
k = n**2
rows = int(input("enter number of rows: "))
for i in range(1, rows+1):
    for spaces in range(rows - 1 - i):
        print(' ',end=' ')
    for x in range(1,i*i):
        if x%i == 0:
            for k in range():
                print(k , end='')