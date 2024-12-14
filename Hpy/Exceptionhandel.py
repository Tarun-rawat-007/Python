# try except is used
a=input("Enter a:")
print("multiplication table of ",a ,"is:")


try:
 for i in range(1,11):
    print(a," X" ,i," = " ,int(a)*i)
except Exception as e:
  print(e)

finally:
  print("finally block code always executed")

print("End of code")
print("End of program here")


# finally also used for clean ups