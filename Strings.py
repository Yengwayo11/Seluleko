#def isDoubloon(string):
    #string = string.lower() #change every character to lowercase
    #for letter in string:
        #if string.count(letter) == 2 : #count function that counts that particula letter in the string
            #print(True)
            #break
        #else:
            #print(False)
#isDoubloon("noon")

#Palindrome strings
def isPalindrome(s):
    s = s.lower() 
    newstring = ''
    char = ["!","?",".",",","*",""]
    for l in s:
        if l not in char:
            newstring += l
        else:
            continue
    if newstring == newstring[::-1]:
        print("it is A palindrom")
    else:
        print("it is not")
isPalindrome("rotator!")

#ccount in string
#s = "Seluleko"
#k = s.count("l")
#print(k)
#def howMany(s, c):
    #v = "a,e,i,o,u"
    #k = []
    #for letter in s:
        #if letter not in v:
            #k.append(str(letter))
        #else:
            #continue
    #howmany = len(k)
    #print(howmany)
#howMany("lllllll", "")

##REMOVE PUNCTUATION
#def removePuntuation(s):  #input any string/sentence
    #v = "!",".",",","?", " "
    #newWord = ""
    #for char in s:
        #if char in v:
            #continue
        #else:
            #newWord += char
    #print(newWord)
#removePuntuation("I LOVE YOU DAMMIT!")

#Numerology
#s = input("enter a name: ")
#sumword = 0
#for letter in s:
    #sumword += ord(letter) - 96
    
#print(sumword)

#word garbler
#import random
#n = "hello"
#idx = 0
#while idx < len(n):
    #for letter in n:
        #if letter == n[] or letter == n[idx]:
            #print(letter, end='')
        #else:
            #print(letter,end='')
    #idx += 1
    
    