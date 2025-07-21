#squarefree numbers
import math
x = int(input("enter any integer: "))
integers = range(2, x)
p = list(integers)
divisors = []
for k in range(2, x+1):
    if x%k == 0:
        divisors.append(k)
perfect_squares = []
for m in divisors:
    if m**0.5 in p:
        perfect_squares.append(m)
    elif m**0.5 not in p:
        continue

if len(perfect_squares) > 0:
    print("x is not a squarefreee number")
else:
    print("x is a squarefree number")
    
#FACTORIAL
#x = int(input("enter any integer: "))
#factorial = 1
#for i in range(x, 1, -1):
    #factorial *= i
#print(factorial)

#how many word in a string
#sentence = input("enter you string: ")
#space = " "
#number_of_spaces = 0
#for char in sentence:
    #if char == space:
        #number_of_spaces += 1
    #else:
        #continue
#number_of_words = number_of_spaces + 1
#print(number_of_words)
#y = ''
#x = 0
#while x != -1:
    #x = int(input("enter any number: "))
    #y = y + " " + str(x)
#print(y)
#numbers = "123456789"
#count1 = ''
#count2 = ''
#count3 = ''
#count4 = ''
#count5 = ''
#count6 = ''
#count7 = ''
#count8 = ''
#count9 = ''
#for number in y:
    #if number == "-" or number == "1":
        #pass
    #elif number == "2":
        #count2 += number
    #elif number == "3":
        #count3 += number
    #elif number == '4':
        #count4 += number
    #elif number == '5':
        #count5 += number
    #elif number == '6':
        #count6 += number
    #elif number == '7':
        #count7 += number
    #elif number == '8':
        #count8 += number
    #elif number == '9':
        #count9 += number

#print(len(count2) ,"*", 2, end=' ')
#print(len(count3) ,"*", 3, end=' ')
#print(len(count4) ,"*", 4, end=' ')
#print(len(count5) ,"*", 5, end=' ')
#print(len(count6) ,"*", 6, end=' ')
#print(len(count7) ,"*", 7, end=' ')
#print(len(count8) ,"*", 8, end=' ')
#print(len(count9) ,"*", 9, end=' ')

