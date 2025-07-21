#rows = int(input("enter a number of rows: "))
#for i in range(rows+1):
    #for star in range(i):
        #print("*",end='')
    #print()
    
#rows = int(input("enter a number of rows: "))
#mangaki = int(input('enter number of triangles: '))
#for i in range(rows+1):
    #for l in range(1,mangaki+1):
        #for space1 in range(rows - i):
            #print(" ",end=' ')
        #for star in range(0,(2*i + 1)):
            #print("*",end=' ')
        #for spaces in range(rows - i):
            #print(" ",end=' ')
    #print()
    
def sum_digits(n):
    sum = 0
    count = 0
    while n > 0:
        k = n%10
        sum += k
        n = n//10
        count += 1
    return sum

for n in range(1,1000000):
    selu = sum_digits(n)
    if n%selu == 0:
        print(n, "sum:",selu)
    else:
        continue

