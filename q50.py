#Develop a Python program that will :
#(1) prompt for the input
#(2) extract all the vowels in the input string and make them lower case
#(3) add all the nonduplicate vowels(aeiou) and
#(4) print the number of trials that you did to collect the 5 vowels .
#Q50

value = "Enter a string"
value_lowercase= value.lower() # check syntax

vowels_1 = "a,e,i,o,u,A,E,I,O,U" # don't need to check capital alphabets
vowels_2 = "a,e,i,o,u"
count=[0,0,0,0,0]
vowels_len = len(vowels_2)

temp_str = ""

for e in value_lowercase:
    if e in vowels_2:
        x=vowels_2.index(e)
        count[x]=count[x]+1
        temp_str = temp_str + e
