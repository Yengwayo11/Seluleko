rows = int(input("enter number of rows: "))
for i in range(rows):
     for stars in range(1,i+1):
          print(" *",end="")
     for spaces in range( 2*(rows)):
          print(" ", end='')
     for star in range(i+1):
          print("*",end='')
     print()