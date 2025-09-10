#operators: used to perform operations over the data / maipulate the data
#operands: values/variables on which operators perform manipulations.

import math


a = 5
b = 6
sum = a + b * 3/3 

#type of operators:
"""1.arithmetic operators: + , -,*,/,//,%"""
#lib_name.fucntion_name(*args)
div = math.floor(a/b)
div2 = math.ceil(a/b)
print(div)
print(div2)
#if the no. is an integer than ciel and floor value is same
#ciel gives high value
#floor gives down value


# modulus
mod = a%b
print(mod)


#exponentiation:
# a^b => a**B
# a: base, b: exponential power
exp=a**b
print(exp)

#example: a = 10 ,b = 10 , 
a = 10
b = 10
exp = a**b
print(exp)

#given a and b , find a^b such that the answer should not exceed 100007.
# 0 <= a,b <= 100
#solution:
ans= (a**b)%100007
print(ans)



"""2. Assignment operations:"""

"""3. comparision operations:"""
a = 5
b = 9
# a += b

print(a >=b)
# if a is greater than or equal to b
print(a <= b)
#if b is greater than or eqaul to a

"""4.logical operations """
#Q2. take two integers and swap them without using an extra variable.
temp = a
a = b
b = temp
print(a,b)                


# given a,b,c print true if a>b and b>c otherwise print false
# using and operators, so true and true gives true, false abd false gives false, true and false gives false
a = 10
b = 5
c = 3
print((a>b) and (b>c) and (a>c))


#using or operators, so if tge expression is true and true gives true, true and false is true, false and false is false.
# #OR operators
# 3 exp 1 or exp 2
# T or T=T
# T or F=T
# F or T=T
# F or F=F

print(((a<b) or (b>c)) and (a<c))

#Q3. take principal amount , rate of interest,
# and time (in years) as integer inputs and calculate simple interest.

principal = int(input("enter the princiapl amount"))
rate = int(input("enter the rate"))
time = int(input("enter the years"))

simpleInterest= (principal*rate*time) /100
print("the simple interest is",simpleInterest)


#Q4. write a program to take the basic salary as
# integer input and calculate the total salary,
# assuming house rent allowance (HRA) is 20% of baisc and travel allowance
# (TA) i 10% of baisc.
basic_salary = int(input("enter your basic salary")) 
house_allowence = basic_salary*20/100
travel_allowance = basic_salary*0.1
total_salary = basic_salary+ house_allowence+ travel_allowance
print(total_salary)

#Q5. write a program to take coordinates of two points
# (x1,y1) and (x2,y2). calculate the distance between 
# them using the distance formula.
"""
print(math..sqrt(4))
print(4**0.5)
"""
x1 = (input("enter the value of x1"))
x2 = (input("enter the value of x2"))
y1 = (input("enter the value of y1"))
y2 = (input("enter the value of y2"))
distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
print(distance)


#Q6: a student enters marks for 3 subjects as strings.
#convert them to integers and calculate the average.
subject_1 = input("enter your marks")
subject_2 = input("enter your marks")
subject_3 = input("enter your marks")

average_marks = (int(subject_1) + int(subject_2) + int(subject_3))/3
print(average_marks)
                 


#Q7: take a number age = 25
#convert it into a string and print "my age is 25"
age = 25
age_string= str(age)
print("my age is ",age_string)

#Q8: a shopping site shows price as string "499.99"
# add delivery charge (50 as int) and print the final bill.

price = float("499.99")
price += 50
print(price)

"""homework"""
#Q9: take a ccomplex no z = 5 + 2j
# convert it into string.                                  
# extract real and imaginary parts as integers.
# print their sum.

z = str(5 + 2j)
z_real = z.split('+')[0].strip()
z_img = z.split('+')[1][1]
print(z_real,z_img)


"""5. Bitwise operator""" 
# Q10. a pen costs $12, a notebook costs $45.
# if you buy 3 pens and 4 notebooks , find the total cost.
pen = 12
notebook = 45

pen = 3*pen
notebook= 4*notebook
total_cost = pen + notebook
print(total_cost)

# Q11. a student scored 78 marks in maths.
#the passing mark is 40. check and print whether the student passed.print true or false accordingly.

score= 78 
passing_marks= 40
check = (score>=passing_marks)
print(f"the result is {check}")

"""homework"""
#Q12.an exam allows a candidate to pass if:
#marks in theory >= 40 
# marks in practical >= 20
#chack if a student with theory = 55 , practical = 15 passed or failed.
theory = 55
practical = 15
theory = (theory>=40)
practical = (practical>=20)
print("the total scor is",theory and practical)

#Q13. CHECK if a letter exists in a given word.
# word = "PYTHON"
a = "a"
word = "python"
print("a is word")


"""7. identity operators:""" #to check the identity of two variables.
#pointing to same object.
a = 2
b = 2
print(a is b)
print(a is not b)

"""8.membership operator:"""
a = 'm'
s='raman'
print(a not in s)
print(a in s)






