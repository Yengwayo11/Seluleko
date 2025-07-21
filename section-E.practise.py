#-31 even or odd
x = int(input("enter the value of x: "))
if x%2 == 0:
    print("even")
else:
    print("odd")
    
# random number between 1 and 100
import random
i = [random.randint(1,100)]
if len(i)== 1:
        print(i)
 #4
for x in range(2,21,2):
    print(x)
    x += 1

#34.
n = int(input("enter the value of n: "))
sum_to_nth_term = n/2 *(1 + n)
print(sum_to_nth_term)
    
#3]
for i in reversed(range(1,11)):
    print(i)
for i in range(10,0,-1):
    print(i)
    
print(not(55<5) and 3> 2)