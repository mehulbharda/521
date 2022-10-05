#Develop a Python program that will :
#(1) prompt for the input
#(2) extract all the vowels in the input string and make them lower case
#(3) add all the nonduplicate vowels(aeiou) and
#(4) print the number of trials that you did to collect the 5 vowels .
#Q50

value = input("Enter a string")
value_lowercase= value.lower() # check syntax

print(value_lowercase)

vowels = "a,e,i,o,u"

count=[0,0,0,0,0]

vowels = len(vowels_2)

temp_str = ""

for e in value_lowercase:
    if e in vowels:
        x=vowels.index(e)
        count[x]=count[x]+1
        temp_str = temp_str + e
