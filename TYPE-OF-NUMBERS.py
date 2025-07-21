def is_armstrong():
    digits = [ int(d) for d in str(number)]
    sumnumbers = []  #where i will store my digit raised to the length of number
    for d in digits:
        powered = d**len(digits)
        sumnumbers.append(powered) #ukufaka kwiList yami lekaSUMNUMBERS   
    return sum(sumnumbers) #since uSUMNUMBER esephethe izinumber ezineEXPONENT
number = int(input("enter the number: "))
if is_armstrong() == number:
    print(True)
else:
    print(False)
    
#Electricity usage
