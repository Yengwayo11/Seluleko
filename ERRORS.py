#numwords = 0
#numBs = 0
#longest = ""

#word = input("enter a word:")
#while word != "$":
    #numwords += 1
    #if word[0].upper() == "B":
        #numBs += 1
    #if len(word) > len(longest):
        #longest = word
    #print(word)
    #word = input("enter another word:")

#if numwords > 0:
    #print("There were", numwords, "words.")
    #print("The longest word was", longest)
    #print("There were", numBs, "words beginning with B.")
#else:
    #print("No words were entered.")

#def isPrime(x):
    #count = 0
    #isprime = True
    #for i in range(2,x):
        #if x%i == 0:
            #count += 1
        #else:
            #continue
    #if count > 0 :
        #print("")
    #else:
        #return isprime
#print(isPrime(17))
##def reverse(x):
    ##Reversed = 0
    ##while x > 0:
        ##m = x % 10
        ##Reversed = Reversed * 10 + m
        ##x = x // 10
    ##return Reversed
##x = int(input("enter a number: "))
##y = reverse(x)
##print(y)
###n = int(input("enter a number: "))
##while n > 0:
    ##for i in range(100):
        ##if isPrime(i) and reverse(i) == 
        
#def Reduce(x):
    #if x < 0:
        #print("Error")
    #else:
        #digits_of_x = [int(d) for d in str(x)]
        #SUM = sum(digits_of_x)
        #while SUM > 9:
            #digits_of_SUM = [int(k) for k in str(SUM)]
            #SUM = sum(digits_of_SUM)
        #return SUM
#x = int(input("enter value: "))
#while x != 0  :
    #print(Reduce(x))
    #x = int(input("enter a value: "))

##def isFunny(x):
    ##x.lower()
    ##reverse = x[::-1]
    ##ord_of_reverse = []
    ##ord_of_x = []
    ##for letter in x:
        ##ord_of_x.append(ord(letter))
    ##for k in reverse:
        ##ord_of_reverse.append(ord(k))
    ##difference = []
    ##for m in ord_of_x:
        ##z = (m+1) - m
        ##difference.append(z)
    ##difference2 = []
    ##for p in ord_of_reverse:
        ##w = (p+1) - p
        ##difference2.append(w)
    ##abalinganayo = []
    ##abangalingani = []
    ##for i in range(len(difference)): 
        ##if difference[i] != difference2[i]:
            ##abangalingani.append(i)
        ##elif difference[i] == difference2[i]:
            ##abalinganayo.append(i)
    ##print(ord_of_x)
    ##print(ord_of_reverse)
    ##print(difference)
    ##print(difference2)
    ##print(abalinganayo)
    ##print(abangalingani)
        
##x = input("enter any string: ")
##y = isFunny(x)
##print(y)     #####not done yet

def reverseWords(inStr):
    x = inStr.split(" ")
    reversedd = x[::-1]
    newsentence = ""
    count = 0
    for i in reversedd:
        newsentence = newsentence + " " + i
        count += 1
    print(newsentence)
    return  count
print(reverseWords("   How are you feeling?"))
longest = 0
n = input("enter a sentence: ")
while n != "-":
    count1 = reverseWords(n)
    n = input("enter a sentence: ")

