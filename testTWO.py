k = 0
while k < 5:
    m = k
    while m > 0 and k < 3:
        m -= 1
        k+=1
    k +=1
print(k)

a = 1
while a < 4:
    b = a
    while b < 3:
        if b%2 == 0:
            b +=1
            continue
        b += 2
    a += 1
print(a)

count = 10
while count >= 0:
    if count % 2 == 0:
        print("Python")
        count -=1
    elif count %3 ==0:
        print("Python")
        count -= 2
    else:
        count -= 3

x = 30
while x>= 0:
    if x % 5 == 0:
        x -= 5
    else:
        x += 1

count = 0
for i in range(-5,5,2):
    count += 1
    i += 5
print(count)

x = 0
for i in range(10,2,2):    # -(3 or 4)
    x += i
print(x)

x = 0
for i in range(10,-5,-3):
    if i%3 == 0:
        continue
    if x > 15:
        break
    x += i
print(x)

z = 9
while z > 0:
    if z % 3 == 0:
        z -= 3
        continue
    if z % 6 == 0:
        z -= 2
    else:
        break
    print(z, end=' ')
print("STOP")

for i in range(2):
    print("?", end="")
    for j in range(3):
        print("a", end="*")
print("X", end="")

for i in range(2):
    print("?", end="")
for j in range(3):
    print("a", end="*")
print("X", end="")

