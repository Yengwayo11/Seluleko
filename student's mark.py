mark = int(input("enter a mark in percentage: "))
if mark >= 80 :
    print("A")
elif 60 <= mark < 80 :
    print("B")
elif 50 <= mark < 60 :
    print("C")
elif mark < 50 :
    print("Fail")
    
#eligible to vote or not
age = int(input("enter age: "))
if age >= 18 :
    print("eligible to vote")
else :
    print("ineligible")
    
# leap year or not
year = int(input("enter a year: "))
if year%4 == 0 and year%100 != 0 :
    print("it a leap year")
else :
    print("it not a leap year")

# discount on bills
amount = float(input("enter amount: "))
percent_for_discount = 3
total = amount*(1 - percent_for_discount/100 )
if amount > 500:
    print(total)
else :
    print(amount)
    
numb1 = int(input("enter numb1: "))
numb2 = int(input("enter numb2: "))
numb3 = int(input("enter numb3: "))

if numb1 > numb2 and  numb3:    
    print(numb1)
elif numb2 > numb1 and  numb3:
    print(numb2)
elif numb3 > numb1 and numb2:
    print(numb3)
    
# salary bonus
salary = float(input("enter salary: "))
bonus_percent = int(input("enter bonus_percent: "))
years_of_service = int(input("enter years_of_service: "))
salary_with_bonus = salary*(1 + bonus_percent/100 )**years_of_service 
salary_bonus = salary_with_bonus - salary

if years_of_service < 1:
    print(salary)
else :
    print(salary_bonus)

integer = int(input( " enter a integer : "))
if 1<= integer <= 10 :
    print("small")
elif 11<= integer <= 50:
    print("medium")
elif integer > 50 : 
    print("large")
