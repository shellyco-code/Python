#iterative statements:
# mathematical equation
# we want to itearate over certain set of instructions,
# then we use iterative statements

#!. for loop, while loop, do while loop.

#1. FOR LOOP:
print("Shells")


"""#print your name 10 times.
# syntax:
# for iterator in range(start,end ,step) , by default step is 1
# this loop starts from start and 
# ends at 'end-1', where iterater is a integer variable"""

for i in range(0,10):
    print("shellssss")

for i in range(10):
    print("shelly-",i)

# Q2:- print only even numbers from 1-10

for i in range(11):
    if (i%2==0):
        print(f"{i} is a even number")

# Q3:- find the sum of first n natural numbers and print the sum.
n = int(input("enter the n numbers"))
sum = 0
for i in range  (0,n + 1):
    sum = sum +i
    
    print(sum)

#2. WHILE LOOP:
# while condition:
#statements
#prit name using wl

i=0
while i<10:
    print("shellssss")
    i +=1


#print even numbers only from 1-10.
i = 0
while i<10:
    if(i%2==0):
        print(f"{i} is the even number")
    i +=1

n = int(input())
sum = 0
while i<=n: 
   sum = sum+1
   i +=1
print(sum)

#Q6. factorial of a number.

fac = int(input("enter the no."))
i,faci = 1,1
while i<= fac:
    i = i+1
print(faci)


#Q7. Fibbonacci series
# given n find nth term of Fibbonacci series.
# using for loop
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c 

#using while loop:-
nth = int(input("find nth term of fibbonacci   series"))
n1,n2 = 0,1
print(n1)
print(n2)
i = 2
while i<nth:
    c = n1+n2
    print(c)
    n1=n2 
    n2=c
    i +=1 
    
# Q8. given three integers a ,b,c find maximum of three and print it.
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))

# solution 1
if (a>=b and a>=c):
    print(f"{a} is the max value")
elif (b>=a and b>=c):
    print(f"{b} is the max value")
elif (c>=a and c>=b):
    print(f"{c} is the max value")
elif(a==b==c):
    print(f"{a}is the max value")


#solution 2 
print(max(a,b,c))

#Q9. given four integers a,b,c,d find max of these 4. (homework problem)
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
d = int(input("enter the number"))

if (a>b and a>c and a>d):
    print(f"{a} is the max value")
elif(b>a and b>c and b>d):
    print(f"{b} is the max value")
elif(c>a and c>b and c>d):
    print(f"{c} is the max value")
elif(d>a and d>b and d>c):
    print(f"{d} is the max value")
elif(a==b==c==d):
    print(f"{a} is the max value")
    

#Q10. check whether a given year is a leap year or not.
# leap year if divisible by 400, or divisible by 4 but not 100.

leap = int(input("enter the year"))
if((leap%100!=0 and leap%4==0 )or leap%400==0):
    print("it is a leap year") 
else:
    print("it is not a leap year")

#Q11. create a python game where the user plays rock-paper-scissors against the computer until they type "quit".
#the computer's choice should be random.

import random
a = 1
b = 6
print(random.randint(a,b)) #generates random numbers between a and b.
# inclusive.



