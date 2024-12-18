##STRINGS
#> Strings is data type that stores a sequence of characters.

str1 = "This is a string. \nWe are creating it in python."
print(str1)        

#>Escape Sequence characters :-   "\n" , "\t"
#       here in upper coding "\n" is used for getting the next sentence in next line.
#       here in upper coding "\t" is used for getting space of between 1st sentence and the next sentence.


## BASIC OPERATIONS
#>> Concatenation
#       "hello" + "world"   ---->   "helloworld"

## INDEXING
#>> Length of STR
#       len(str)

str1 = "apna"
str2 = "college"
print(len(str1))
print(len(str2)) 

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))

## SLICING
#> Accessiing parts of a string 
# str[ starting_idx : ending_idx ]  -->  Ending idx is not included 
str = "Apna College" 
#str[ 1:4 ] is "pna"
#str[  :4 ] is same as str[ 0:4 ]
#str[ 1:  ] is same as str[ 1: len(str)]
print(str[1:8])
print(str[ :4])     #[ 0:4 ]
print(str[1:])      #[ 5:len(str)]


## SLICING ( NEGATIVE INDEX )
str = "Apple"
#str[ -3:-1]  is "pl"
print(str[ -3:-1])


## STRING FUNCTIONS
str = "i am studing python from ApnaCollege"
print(str.endswith("ege"))
print(str.endswith("er."))      # Returnd true if string ends with subtr
print(str.capitalize())         # Capitalizes 1st char
print(str)
str = str.capitalize()
print(str)
# str.replace(old, new)         # Replaces all occurrences of old with new
print(str.replace("o", "a"))
print(str.replace("python", "javascript"))
# str.find(word)                # Returns 1st index of 1st occurrer
print(str.find("o"))
print(str.find("from"))
print(str.find("Q"))
print(str.count("am"))          # Counts the occurrence of substr in string
print(str.count("o"))


### Practical / Practice
# Q)  WAP to input user's first name & print its length.
name = input ("Enter Your Name : ")
print ("length of your name is", len(name))

# Q) WAP to find the occurence of '$' in a string
str = "Hi, $I am the $ symbol $99.99"
print(str.count("$"))

            ## ----- X ----- ##


## CONDITIONAL STATEMENT
#> if-elif-else(SYNTAX)
#
#> if(condition) :
#   statement1

age = 15

if(age >= 18):
    print("Can vote & apply for License")
if(age < 18):
    print("can't vote & apply for License")


#> elif(condition) :
#    statement2

light = "yellow"

if(light == "red"):
    print("STOP")
elif(light == "green"):     #IMP:- Before using "elif" condition, 1st we need to use "if" condition
    print("GO")
elif(light == "yellow"):
    print("Slowdown > Look > Then Cross Road")

## Difference between condition "if" and "elif" is :--
  # "if" condition always check statement whereas "elif" condition only checks when "if" condition fails.
num = 5

if(num > 2):
    print("Greater than 2")
if(num > 3):
    print("Greater than 3")

num = 8

if(num > 4):
    print("Greater than 2")
elif(num > 7):
    print("Greater than 3")
#> else :
#   statementN
light = "pink"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("Slowdown > Look > Then Cross Road")
else:
    print("light is broken")

age = 24

if(age >= 18):
    print("Can Vote")
else:
    print("Cannot Vote")

age = 16

if(age >= 18):
    print("Can Vote")
else:
    print("Cannot Vote")
# INDENTATION :- Space we are using after codition statement or anywhere in python.

## PRACTICE ##
marks = 74

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >= 0 and marks < 33):
    grade = "F"
else:
    grade = "D"

print("grade of the student ->", grade)

marks = 29

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >= 0 and marks < 33):
    grade = "F"
else:
    grade = "D"

print("grade of the student ->", grade)

marks = int(input("Enter student marks ->  "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >= 0 and marks < 33):
    grade = "F"
else:
    grade = "D"

print("grade of the student ->", grade)

            ## ----- X ----- ##


## NESTING :-  It means using codition statements into another condition statements
age = int(input("Please Enter Your Age ->  "))

if(age >= 18):
    if(age >= 80):              #Using condition in another condition statement
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")


##  Let's Practice -----

# Q) WAP to check if a number entered by the user is odd or even.
num  = int(input("Enter the Number to check (Even / Odd) =  "))
ren  = num % 2          # Here "%" means remainder

if(ren == 0):
    print("EVEN")
else:
    print("ODD")


# Q) WAP to find the greatest of 3 numbers entered by the user.

a  = int(input("Enter First Number =  "))
b  = int(input("Enter Second Number =  "))
c  = int(input("Enter Third Number =  "))

if(a >= b and a >= c):
    print("First Number is Largest ", a)
elif(b >= c):
    print("Second Number is Largest ", b)
else:
    print("Third Number is Largest ", c)



# Q) WAP to check if a number is a multiple of 7 or not.

x = num  = int(input("Enter Number to check Multiple of 7 =  "))

if(x % 7 == 0):
    print("Multiple of 7 ")
else:
    print("Not a Multiple of 7 ")



## Homework 
# Q) WAP to find the greatest of 4 numbers entered by the user.

a  = int(input("Enter First Number =  "))
b  = int(input("Enter Second Number =  "))
c  = int(input("Enter Third Number =  "))
d  = int(input("Enter Fourth Number = "))


if(a >= b and a >= c and a >= d):
    print("First Number is Largest ", a)
elif(b >= c and b >= d):
    print("Second Number is Largest ", b)
elif(c >= d):
    print("Third Number is largest ", c)
else:
    print("Fourth Number is Largest ", d)


                ## ----- X ----- ##