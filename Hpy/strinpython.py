
print("=========================String in  python=============================\n")
# string in python are immutable
name="tarun rawat"
name2="vicky"
print(name2[0])
#multiline string
name3='''my name 
is  tarun rawat?  
and yours'''
print(name3)

#string methods
names="tarun rawat"
print("length of string is:",len(name))
print("slicing ofstring is:",names[0:4])
print("slicing ofstring is:",names[2:4])
print("upper case string is:",names.upper())
print("lower case string is:",names.lower())
print("replace in string is:",names.replace("a", "o"))
print("split string is:",names.split(" "))   
print("caplize string is:",names.capitalize())   #capltilze first carater
print("center string is:",names.center(50))      # add spaces in string
print("count charcter instring is:",names.count("a")) 
print("ends with instring is:",names.endswith("at")) 
print("find specific char  instring is:",names.find("w")) 
print("find specific char  instring is:",names.isalpha()) 
print("chech if  string is   loercase string is:",names.islower()) 
print("check if  string is   upper case string is:",names.isupper()) 
print("check if  string is   upper case string is:",names.isspace()) 
print("check if  string is   upper case string is:",names.swapcase()) 
print("check if  string is   first char upperstring is:",names.title()) 


# fstring in python
# used for formatting
# {} are used to place variable dynamically
letter="hi my name is {0}  and i am from {1}"
country="india"
name="tarun"
print(letter.format(name,country))
# ese karne a method=fstring
print(f"hi my name is {country}  and i am from {name}")




