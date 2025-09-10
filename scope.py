# scopes of the python
#GLOBAL SCOPE
#LOCAL SCOPE
# global variables cannot be modified in local scope.
a = 10
a = a+10
print(a)
def sqrt(n):
    global a
    a = a+4
    print(a)
    b = 50
    print(b)

sqrt(20)
print(a)
# b is pesent in the local scope. so we have to add global scope to it 

# ARGUMENTS:
# 1. positional arguments:the position of arguments matters.
def substract(a,b):
    print(b - a)

a = 2
b = 3
substract(b,a) #correct
substract(a,b) # incorrect

# 2. keyword arguments: order/ position does not matter
def substract(a,b):
    print(a-b)

# substract b from a
substract(a=2, b =3) #correct
substract(b = 3, a = 2) # correct
# both will give -1 coz the value is fixed order matter nahi karta

# 3. default arguments
def substract(a = 2, b = 3):
    print(a-b)

substract(4,5)
# the passed values are overriding the default values.

# Q 1. write a function that takes marks of 5 subjects amd returns total and average.
a= int(input("enter your marks of maths"))
b= int(input("enter your marks of chem "))
c = int(input("enter your marks phy"))
d= int(input("enter your marks hindi"))
e= int(input("enter your marks eng"))


def subject(a,b,c,d,e):
    total = a+b+c+d+e
    avg = a+b+c+d+e/5
    print(f"the avg of all subjects are {avg}")
    print(f"the total of all subjects are {total}")

    return avg,total

subject(a,b,c,d,e)

#O 2. write a function that takes an integer and returns True if 
# it's a palindrome (n=reads the same forwards and backwards), otherwise  False.
# use loops and conditionals.

def reverse_integer(n):
    num = 0

# 24 --> 42
# 4*10 + 2 -> 42
n = 42
rev_n= 0

rev_n = 0*10 + n%10
n //=10
# rev-n contains 2
# n contains 4

rev_n = rev_n*10 + n%10
n //=10

while n !=0:
    rev_n = rev_n*10 + n%10
    n //=100
print(rev_n)

n = int(input("enter an integer:"))
reverse_integer(n)

