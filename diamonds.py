size = int(input("enter an even number of rows: "))
size = int(0.5*size)
for i in range(size,0,-1):
     for stars in range(i, 0,-1):
          print("*",end=" ")
     for spaces in range(2*(size - i)):
          print(" ",end=" ")
     for stars in range(i ,0,-1):
          print("*",end=" ")
     print()
for k in range(1,size+1):
     for star2 in range(1,k+1):
          print("*",end=" ")
     for spaces2 in range(2* (size - k)):
          print(" ",end=" ")
     for stars in range(1, k+1):
          print("*",end=" ")
     print()