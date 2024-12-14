student={"name":"tarun",
         "age":23,
         }
print(student["name"])
print(student["age"])

for key,value in student.items():
    print(key,value)

student["job"]="read"   #adding new item and value
print(student)