#project4
n = int(input("enter the value of n: "))

for i in range(0, n):
    i+=1
    k = i*1,     i*2,     i*3   
    print(k, end='\n')
    if i == n+1:
        break

for h in range(1,5):
    print("x^", h, end="\t")
print()

for r in range(1, 11):
    
    for c in range(1,5):
        print(r**c, end="\t")
        
    print()
    
#5
n = int(input("enter any number: "))
for i in range(1, n+1):
        print(i*str(i))
#6
die1 = range(1,7)
die2 = range(1,7)
for i in die1:
    for c in die2:
        if i+c == 12:
            print(f"{1000/36000 *100} percent")
        else:
            continue
        
#7
integer = int(input("enter your integer: "))
x = int(input("enter integer backward: "))
if integer == x:
    print(f"{integer} is a palindrome number")
else:
    print(f"{integer} is not a palindrome number")
    
#8

    
            
    