#def countDigits(n):
    #count = 0
    #digits = [int(d) for d in str(n)]
    #for i in range(len(digits)):
        #count += 1
    #return count
#n = int(input("enter your number of interest: "))
#squered = n**2
#leftpart = (squered)//(10**countDigits(n))
#rightpart = (squered)%(10**countDigits(n))
#if leftpart + rightpart == int(n):
    #print("it's a kaprekar")
#else:
    #print("it's not a kaprekar") 
    
def mysterystr(a, b, mystr ):
    newstring = ""
    for i in range(a,b,2):
        if mystr[i] > 'a':
            newstring += "!"
        else:
            newstring += mystr[i]
    return newstring
str1 = "GOODluck"
str2 = mysterystr(0,6,str1)
print(str2)    
        