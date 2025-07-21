#s = "seluleko"
#vowels = "aeiou"
#new = ''
#for l in s:
    #if l in vowels:
        #new += l
    #else:
        #continue
#print(new[-1::-1])

#MNQOBI SI WORKSHEET 1
#sentence = ''
#x = int(input("enter a number of words you want in your sentence: "))
#while x > 0 :
     #word = input(" enter any word: ") #each an everytime ingena kwiLOOP ithatha igama
     #sentence = sentence + " "+ word
     #x -= 1
#print(sentence)

#question 2
def anagrams(x, z):
    s = ''
    x.lower()
    z.lower()
    for letter in x:
        if letter in z:
            s = s + letter
        else:
            continue
    if s == x:
        print("z and x are anagrams")
    else:
        print("z and x are not anagrams")
anagrams("moon", "noom")

##question 3
#string = input("enter any word: ")  #accepts any name from the user
#vowels = "aeiou"
#string.lower()    #even if the entered string is capitilized it will be lowered
#new = ""
#for letter in string:  #checks each an every letter in the string
    #if letter in vowels: #checks whether that letter is a vowel on not
        #continue      #if its a vowel it jumps it and not concatenate with it
    #else:
        #new = new + letter #forms a string without vowels
#print(new[-1::-1]) #prints the reverse of a new formed string

#question 4
#def fullname(first, middle, last):
    #print(last, first,middle[0])
#fullname("Seluleko", "Mhlengi", "Magwaza")

##question 5
#def count():
    
    