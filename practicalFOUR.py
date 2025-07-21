#2
integer = int(input("enter your integer: "))

for i in range(integer+1,0,-1):
    if integer%i == 0:
        print(i, end='\t')
        i+=1
    else:
        continue

#4
n = int(input("enter the value of n: "))

for i in range(0, n):
    i += 1
    k = i * 1, i * 2, i * 3
    print(k, end='\n')
    if i == n + 1:
        break