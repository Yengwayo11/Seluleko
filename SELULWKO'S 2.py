num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 // num2)
    
x = 12
y = 5
print(x*y)

a = 25
b = 4

print(a + b)
print(a - b)
print(a%b)

name = 'Alice'
age = 22
city = 'Paris'
print(f"{name} is {age} years old and lives in {city}")

x = 8
z = 3
result= z*x
print(f"the results of 8 multiplied by 3 is {result}")

exam1 = int(input("enter a mark in percentage: "))
exam2 = int(input("enter a mark in percentage: "))
exam3 = int(input("enter a mark in percentage: "))

if exam1>= 50 and exam2 >= 50 and exam3 >= 50:
    print('PASS')
elif exam1 >= 50 and exam2 >= 50 and 40<= exam3 <50 and (exam1 + exam2 + exam3)/2>= 50:
    print('SUPPGRANTED')
else:
    print("FAIL")
