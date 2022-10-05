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


temp_str = ""

for e in value_lowercase:
    if e in vowels:
        x=vowels.index(e)
        print(x)
        count[x]=count[x]+1


for count, ite in enumerate(count):
    if ite == 1:
        temp_str = temp_str + vowels[count]

print(temp_str)
