def growingStars(int1,int2,int3):
     for p in range(3):
          for i in range(1,int1):
               print("*",end='')
          for k in range(int2):
               print("+")
          for l in range(int3):
               print("#")
     print()
growingStars(7,3,4)
    