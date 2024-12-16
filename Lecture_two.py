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

#> else :
#   statementN
