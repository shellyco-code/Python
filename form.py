# form filler
# User enter name , age , marks -> all strings -> convert appropriately
# Display a formatted messagname

name=str(input("enter your name "))
age=int(input("enter your age "))
marks=float(input("enter your marks "))

name=str(name)
age=str(age)
marks=str(marks)

print("name:",name)
print("age:",age)
print("marks:",marks)

print(f"the user named{name} age{age} obtained marks{marks}") #f is formating tag 
