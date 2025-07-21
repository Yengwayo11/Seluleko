import random
l = random.randint(1,11)
for i in range(1,11):
    if i == l:
        print("you got it right")
        break
    else:
        print("try again")
        break

