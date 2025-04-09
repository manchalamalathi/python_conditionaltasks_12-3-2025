# Task:- 
# 1.Write a Python program that takes an integer as input and prints whether it is even or odd.
number=int(input("please enter a number : "))
if number%2==0:
    print(number," is a even number ")
else:
    print(number,"is a odd number")


# 2.Write a program that takes two numbers as input and prints the larger number. If they are equal, 
# print "Both numbers are equal".
number1=int(input("please enter a first number : "))
number2=int(input("please enter a second number : "))
if number1>number2:
    print(number1,"is larger")
elif number2>number1:
    print(number2,"is larger")
else:
    print("both are equals")    


# 3.Write a Python program that asks the user for a number and prints whether it is positive, negative, or zero.

number=int(input("please enter a number  : "))
if number>0:
    print(number,"is positive number")
elif number<0:
    print(number,"is a negative number")
else:
    print(number,"is zero")    



# 4.Write a program that asks the user for their age. If the age is 18 or above, print "You are eligible to vote", otherwise print "You are not eligible to vote".
age=int(input("please enter your age : "))
if age==18 or age>18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")    



# 5.Write a program that takes a student's marks (out of 100) and prints:
# "Pass" if marks are 40 or more
# "Fail" if marks are less than 40
marks=int(input("please enter your marks : "))
if marks<=100 and marks>=40:
    print("you are passed")
elif marks>100:
    print("please enter your marks  out of 100")
else:
    print("fail")    
