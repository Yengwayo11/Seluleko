#n = int(input("enter a numer: "))
#w = []
#sum = 0
#count = 0
#while n > 0:
    #k = n%10
    #w.append(k)
    ##sum = sum*10 + k
    #n = n//10
    #count += 1
#print((w))
#question 1
height = float(input("enter height: ")) #using float so that it can accept decimal inputs
weight1 = float(input("enter old weight: "))
count = 0   # this counts the number of overweights
for i in range(1,12+1):
    #count = 0   # this counts the number of overweights
    sum_weight2 = 0   #to calculate the average at the end
    weight2 = float(input("enter weight for month in kg: "))
    BMI = round(float(weight2/(height*height)), 1)
    percentage_change = round(((weight2 - weight1)/weight1) * 100 , 1)
    if BMI < 18.5:
        print(i , weight2, BMI , percentage_change, "underweight")
        sum_weight2 += weight2
    elif BMI >= 18.5 and BMI < 25 :
        print(i , weight2 , BMI , percentage_change, "normal" )
        sum_weight2 += weight2
    elif BMI >= 25 and BMI < 30 :
        print(i , weight2 , BMI , percentage_change, "Overweight" )
        sum_weight2 += weight2
        count += 1
    elif BMI >= 30 :
        print(i , weight2 , BMI , percentage_change, "Obese" )
        sum_weight2 += weight2
        
average_weight = round((sum_weight2)/12)  #calculate average  
print("average weight : ",average_weight)
print("number of overweight: ", count)

def reverse(n):
    reversed_n = 0
    while n > 0:
        m = n%10    #start by taking the last digit to reverse
        reversed_n = reversed_n *10 + m
        n = n//10
    return reversed_n
print("reverse-divisible")
for i in range(1,1000000):
    x = reverse(i)
    if i%x == 0:
        print(i)