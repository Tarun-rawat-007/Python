s="hello world"
print(len(s))    #length of string
print(sorted(s))   #sorted string
print(max(s))     #max string
print(min(s))    #min dtring
print(s.lower())  #lower case srting
print(s.upper())  #uppercase srtring
print(s.split())   # split string



list=["tarun","rawat"]
word="hi"
# joins list items only
print("join keyword:",word.join(list))
# find
print("Find function:",word.find("hi"))
# replace
newword=word.replace("hi",'hello')
print("Replace funtion",newword)

name="tarun"
rs=""

for char in name:
    rs=char+rs
print(rs)
name2="vicky"
print(name2[::-1])  #Reverse String

print("Capital first letter:",name.title())   #capital first letter


str="my name is tarun rawat"
words=str.split()
rw=" ".join(words[::-1])
print(rw)
print(rw[::-1])