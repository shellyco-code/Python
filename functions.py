# functions:- code blocks which are created to increase reusability , modularity ,  cleanliness , readable , understandable.
# DRY - don't repeat yourself

#syntax:
# definition of a function:
def name_of_function(*args):
    pass

#Q1. write a function to perform addition of two integers a and b.

a = int(input("enter the number"))
b = int(input("enter the number"))

# def add(a,b):
#     sum = a+b
#     return sum 

#  print(add(a+b))

#Q2. write a function greet(name) that prints a personalized greeting message.
name = input("enter name")

def greet(name):
    print(f"{name} welcome to pst")
    return(f"{name} hello have a nice day")
print(greet(name))


# Q3. write a function add(a,b) that takes two numbers and prints their sum. call it using positional arg.
a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
def add(a,b):
    sum = a + b
    print(f"the sum of {a} and {b} is: {a+b}")
# calling the function / invoke the function
add(a,b)

#Q4. write a function square(num) that returns the square of a number.

num = int(input("enter the number"))
def square(num):
    return(num*num)
print(square(num))

#Q5. write a function that returns both the area and perimeter of a rectangle.

len = int(input("enter the length of the rectangle"))
width = int(input("enter the width of the rectangle"))

def area_and_perimeter(len , width):
    area = len * width
    perimeter = 2*(len + width)
    return area, perimeter
print(area_and_perimeter(len,width))

#Q6. write a function factorial(n) that returns the factorial of a number.
def factorial(n):  
    if n == 0:
        print(1)
    else:
      #fact=1*2*3*4*5.....
      for i in range(1,n+1):
        fact = fact*i
    print(fact)


    





