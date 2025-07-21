def trianglereplicated(rows,mangaki):
   for i in range(1,rows+1): # for each line
      for k in range(1,mangaki+1):
         for stars in range(1,i + 1):
            print("*",end=" ")
         for spaces in range(2*(rows - i)):
            print(" ",end=" ")
         for stars in range(1,i + 1):
            print("*",end=" ")
      print()
   return 
x = trianglereplicated(5,6)
print(x)