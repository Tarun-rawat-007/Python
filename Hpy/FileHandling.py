# file=open('hello.txt','r')   #select file

# text=file.read()    #select text
# print(text)         # print text


# # writing in afile
# file=open('hello2.txt','a')   #select file
# file.write("\nhello tarun")

# with open('hello2.txt','a') as f:
#     f.write("hii best way ")



f=open('hello2.txt','r')   #This will reda wholwe lines in a file and return in array form 
while True:
    line=f.readlines()
    if not line :
        break
    print(line)
    print(f.tell())    # tell current position

  