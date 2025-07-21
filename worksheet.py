def is_armstrong():
    new = []
    n = int(input("enter a number: ")) #example 123
    while n > 0:
        k = n%10   #1st [3]
        new.append(k)
        n = n//10
    return new
x = is_armstrong()
def powerednumbers():
    for i in x :
        l = i**len(x)
        print(l)
g = sum(int(powerednumbers(123)))