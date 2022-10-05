
#Develop a Python program that will :
#(1) prompt for the input
#(2) extract all the vowels in the input string and make them lower case
#(3) add all the nonduplicate vowels(aeiou) and
#(4) print the number of trials that you did to collect the 5 vowels .
#Q50

value = input("Enter a string")
value_lowercase= value.lower() # check syntax

print(value_lowercase)

vo = "a,e,i,o,u"

count=[0,0,0,0,0]


temp_str = ""
ts = ""

for e in value_lowercase:
    if e in vo:
        ts = ts + e
        x=int(vo.index(e)/2)
        print(x)
        count[x]=count[x]+1
print(ts)


for count, ite in enumerate(count):
    if ite == 1:
        temp_str = temp_str + vo[count*2]

print(temp_str)