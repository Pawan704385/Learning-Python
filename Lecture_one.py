name = "Pawan"
age = 21
price = 25.99
print(name, age, price)
print("my name is:", name)
print("my age is :", age)


a= 2
b=5
sum = a + b
diff = b-a
print(sum)
print(diff)

print("Hello World ")
# Just practicing
# no need to print this 
# its also called coment

print("changed run code's shortcut key to 'ctrl+r'")
##arithmatic operaors
#( + , - , * , / , % , ** )
a = 5
b = 2
sum = a + b  
print (sum)
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a % b)  # here '%' means modulo uses for finding remainder
print (a ** b)  # here '**' stands for power, means a^b

##Relational / Comparison Operators
#( == , != , > , < , >= , <= )
a = 50
b = 20
print (a == b)   #False  # here '=='  means Equals 
print (a != b)   #True   # here '!='  means Not Equals
print (a >= b)   #True   # here '>='  means Greater than Equalto
print (a > b)    #True   # here '>'   means Greater


##Assignment Operators
#( =, +=, -=, *=, /=, %=, **=)
num = 10
num = num + 10    #10 + 10 ==20  #here 'num + 10' means Addition
num = 10
num += 10       #here '+=' means Addition
print ("num  : ", num)
num = 10
num -= 10       #here '-=' means Substraction
print ("num  : ", num)
num = 10
num *= 10       #here '*=' means Multplication
print ("num  : ", num)
num = 100
num /= 5        #here '/=' means Divide
print ("num  : ", num)
num = 10
num %= 10
print ("num  : ", num)
num = 10
num **= 2       #here '**=' means Power
print ("num  : ", num)

##Logical Operators
#( not, and, or)
print (not True)       #here 'not True'  stands for False
print (not False)      #here 'not False' stands for true
print (not (a > b))
val1 = True
val2 = False
print ("and operator:", val1 and val2)
print ("or operator:", val1 or val2)
val1 = True
val2 = True
print ("and operator:", val1 and val2)


##TYPE CONVERSION
# ( a, b = 1, 2.0
#    sum + a+b)
# (error
#       a, b = 1, "2"
#       sum + a+b
a = 2
b = 4.25
sum = a+b
print(sum)
# a = "2"
# b = 4.25
# sum = a+b
# print(sum)  #here "2" creates ERROR as can't convert string into float automatically

## TYPE CASTING
#(  a, b = 1, "2"
#      c = int(b)
#       sum = a + c)
a = int("2")
b = 4.25
print(type(a))
print(a+b)

a = float("2")
b = 4.25
print(type(a))
print(a+b)
