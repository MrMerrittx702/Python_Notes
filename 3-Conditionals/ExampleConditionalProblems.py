
'''Example Problems with boolean expressions'''





'''Example Problems with Conditionals'''


#Determine if a number is even or odd
num = 0

if(num % 2 == 0):
  print("even")
else:
  print("odd")

#Determine if a number is positive negative or 0
num = 0

if(num > 0):
  print("positive")
elif(num < 0):
  print("negative")
else:
  print(0)

#Given two numbers determine which one is larger
a = 4
b = 3

if(a > b):
  print(a)
elif(b > a):
  print(b)
else:
  print("equal")

#Given 3 numbers determine the largest
a = 1
b = 2
c = 3

if(a > b and a > c):
  print(a, "is largest")
elif(b > a and b > c):
  print(b, "is largest")
else:
  print(c, "is largest")


#Determine if a year is a leap year(nested if)
#A leap year is a year that is divisible by 4, except for years that are divisible by 100 but not divisible by 400. 
# 1900 was not a leap year because it is divisible by 100 but not by 400, 
# 2000 was a leap year because it is divisible by both 100 and 400.

year = 2023

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(year, "is a leap year")
    else:
      print(year, "is not a leap year")
` else:
    print(year, "is a leap year")
else:
  print(year, "is not a leap year") 
  `

#Write a program that takes a number from 1 to 12 as input from the user and prints the corresponding month name.
month = 1

if(month = 1):
  print("January")
elif(month = 2):
  print("February")
elif(month = 3):
  print("March")
elif(month = 4):
  print("April")
elif(month = 5):
  print("May")
elif(month = 6):
  print("June")
elif(month = 7):
  print("July")
elif(month = 8):
  print("August")
elif(month = 9):
  print("September")
elif(month = 10):
  print("October")
elif(month = 11 ):
  print("Novemeber")
elif(month = 12):
  print("December")
else:
  print("error")


#Write a program to check if a number is between 0-10 or 10-20 or 20-30.
number = 0

if(0 <= number and number <= 10):
  print(number, "is between 0-10")
elif(10 < number and number <=20):
  print(number, "is between 10-20")
elif(20 < number and number <= 30):
  print(number, "is between 20 and 30")
else:
  print(number, "is not in the range")
  

#Write a program to convert roman numerals to integers
#Limit your answer to these numerals I = 1, V = 5, X = 10, L = 50
numeral = "X"

if(numeral == "I"):
  print(1)
elif(numeral == "V"):
  print(5)
elif(numberal == "X"):
  print(10)
elif(numeral == "L"):
  print(50)
else:
  print("not recognized")



  
