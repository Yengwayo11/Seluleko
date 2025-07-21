stringONE = input("enter any word: ")
stringTWO = input("enter any word: ")
stringONE.lower()
stringTWO.lower()
idx = 0
position = []
distance = 0
for i in range(0,idx):
     for letter in stringONE:
          if letter == stringTWO[idx]:
               continue
    #elif stringONE > stringTWO:
        #distance = len(stringONE) - len(stringTWO)
        #position.append(idx+distance)
    #elif stringONE < stringTWO:
        #distance = len(stringTWO) - len(stringONE)
        #position.append(idx+distance)
          else:
               distance += 1
               position.append(idx)
          idx += 1
print("distance"," ", "position")
print(distance," ",position)