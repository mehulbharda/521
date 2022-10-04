#Develop a Python program that will : 
#(1) prompt for the input 
#(2) extract all the vowels in the input string and make them lower case 
#(3) add all the nonduplicate vowels(aeiou) and 
#(4) print the number of trials that you did to collect the characters.
#Q50

value = "Enter a string"
value_lowercase= value.toLowerCase() # check syntax

vowels_1 = "a,e,i,o,u,A,E,I,O,U" # don't need to check capital alphabets
vowels_2 = "a,e,i,o,u"
vowels_len = len(vowels)

temp_str = ""

for e in value_lowercase:
    if e in vowels:
        temp_str = temp_str + e.lower()
