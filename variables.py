#take two numbers from user and pront the sum of the numbers
a=(input("enter a number"))
b=(input("enter a number"))
s=a+b
print('sum of numbers is ',a+b)

#input radius from user and calculate area of circle
r=int(input("enter the radius of circle"))
a=22/7*r**2
print('the area of the given circle is ',a)

#input length and breadth and find area of rectangle 
l=int(input("enter the length of rectangle"))
b=int(input("enter breadth of rectangle"))
a=l*b
print('the area of the given rectangle is ',a)

#area of a triangle using herons formula
a=int(input("enter the side of triangle"))
b=int(input("enter the side of triangle"))
c=int(input("enter the side of triangle"))
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**1/2
print('the area of the given traingle is ',a)

#square root of a number 
a=int(input("enter a number"))
s=a**1/2
print('the square root of given number is ',s)

#check whether the number is odd or even
a=int(input("enter a number"))
if a==0 or a==1:
    print('no is neither even nor odd')
elif a%2==0:
    print('the given number is even')
else:
    print('the number id odd')

#print max in a,b,c
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("eneter a number"))
if a>=b and b>=c:
    print('the greatest no is a')
elif b>=a and a>=c:
    print('the greatest no is b')
else:
    print('the greatest no is c')

#score card
score=int(input("enter your marks between (1-100)"))
if score<40:
    print('fail')
elif score>=40 and score<=60:
    print('pass')
elif score>=41 and score<=80:
    print('merit')
else:
    print('distinction')  









