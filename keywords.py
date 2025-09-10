# learning keywords :- break , continue , pass

# Break:
# Q1. keep taking numbers until the user enters 0, then print me. 
# first solution
num = -1
sum = 0
while num != 0:
     num= int(input())
     sum += num
print(sum)

# second solution
sum = 0
while True:
     num = int(input())
     if num == 0:\
     sum += num
            
print(sum)

#Q2.Print "i am don" whenever a multiple of 3 appears otherwise
# print "i am pilot"

n = int(input())
for i in range(n):
     if i%3 == 0:
          print("i am don")
          continue   
     print("i am pilot")


#Q3. Reverse a number using while.
# n = 34, 43
# 34%10 = 4 , 34/10 -->3
# 3%10 -->3 , 3/10 -->0


# pass statement :- 
for i in range (5):
  if i==2:
      pass
  else:
      print()




     








