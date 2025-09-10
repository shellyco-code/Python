#type conversion (int, boolean , float . string , character)

# type()
#assignment

x=200
print(type(x))

#reassignment
x = 200.00
print(type(x))

#reassignment
x = True
print(type(x))

#implicit conversion:
x = 5
print(type(x))
x = 5+ 6.2
print(type(x))
x = "rahul" + '5'
print(type(x))

# explicit conversation : int(), float(), str(), bool()
x = int(5.9)
print(x)
x = str(x) + " " + str(5.8)
print(x)
x = bool(x) #if the no. is zero then only it'll give false otherwise true
print(x)


print(int(9.9))
print(float(True)) #converting bool to float so if true its 1.0 for false its 0.
print(str(123) + "abc")

x = 17 + 1
print("my name is shelly" ,x, "year old")

 #string formating
print(f"my name is shelly and i am {17 +1} year old")

#create a simple calculator which takes random values and perform basic arothmetic operations
#like +,-,/,*
# enter the first no. :
# enter the second no. :
# the sum of two a and b is :
#the substraction of b from  a is:
#the division of a by b is:
# the modulus of a by b is:

number_1 = int(input("enter the first number:"))
print(number_1)
number_2 =int(input("enter the second number:")) 
print(number_2)

print(f"the sum of {number_1} and {number_2} is: {number_1 + number_2}")
print(f"the substraction of {number_2} from {number_1} is : {number_1 - number_2}")
print(f"the division of {number_1}by {number_2} is: {number_1/number_2}")
print(f"the modulus of {number_1}and {number_2}is: {number_1*number_2} ")


#form filler:
# user enters name, age, marks -> all strings -> convert appropriately
# display a formated message.