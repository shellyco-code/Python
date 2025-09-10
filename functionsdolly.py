def add():
 a=10
 b=20
 print(a+b)
add()

def display():
 print("skibiddi toilet skiddi rizz")
 a=6
 b=9
 c=a+b
 return c
p=display()
print('the value of p is ',p)

def calsum(x,y):
 s=x+y
 return s

num1=int(input("enter a number"))
num2=int(input("enter a number"))
sum=calsum(num1,num2)
print("sum of two numbers is",sum)

def calall(x,y):
 return x+y,x-y,x/y,x*y

#_main
num1=int(input("enter a number"))
num2=int(input("enter a number"))
add,sub,div,mult=calall(num1,num2)
print("sum is ",add)
print("diff is ",sub)
print("division is ",div)
print("multiplication is ",mult)

def cal(a,b,c):
 s=a+b+c
 return s

def average(x,y,z):
 sm=cal(x,y,z)
 return sum/3

num1=int(input("enter a no"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
print("average of three given numbers is ",average(num1,num2,num3))


