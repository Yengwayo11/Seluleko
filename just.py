n = int(input("enter a numner: "))
for i in range(n):
    for spaces in range(1,n+1):
        print(" ", end=" ")
    for num in range(1,n+1):
        print(i, end=" ")
    print()