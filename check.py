rows = int(input("enter number of rows: ")) #lines the triangle will have
for row in range(rows):                     #for each line/row
    for spaces in range(rows - 1 - row):# rows - 1 - row---check for space trend
        print(" ",end='')
    for k in range(row + 1):  #from 2k + 1 of odd number
        print("*",end='')           #row + 1,0,-1
    print()