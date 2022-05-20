# 1
# a='banana'
# b=a.upper()

# print(f"The Upper case of 'banana' is: {b}")
# 2
# natural_number_list=[1,2,3,4,5]
# print(5 in natural_number_list)
# 3
# num1= int(input("Enter a first number: "))
# num2= int(input("Enter a second number: "))
# num3= int(input("Enter a third number: "))
# if num1<num2 and num1<num3:
#     print(f"The smallest number is {num1}")
# elif num2<num3 and num2<num1:
#     print(f"The smallest number is {num2}")
# else:
#     print(f"The smallest number is {num3}")
# 4
# num1= int(input("Enter a first number: "))
# num2= int(input("Enter a second number: "))
# num3= int(input("Enter a third number: "))
# total=num1+num2+num3
# print(f"The sum of the given numbers: {total}")

# 5
# print("MONTH CALDULATOR")
# month= int(input("Enter a number from 1 to 12: "))

# if month==1:
#     print(" MONTH: JANUARY")
# elif month==2:
#     print("MONTH: February")
# elif month==3:
#     print("MONTH: MARCH")
# elif month==4:
#     print("MONTH: APRIL")
# elif month==5:
#     print("MONTH: MAY")
# elif month==6:
#     print("MONTH: JUNE")
# elif month==7:
#     print("MONTH: JULY")
# elif month==8:
#     print("MONTH: AUGUST")
# elif month==9:
#     print("MONTH: SEPTEMBER")
# elif month==10:
#     print("MONTH: OCTOBER")
# elif month==11:
#     print("MONTH: NOVEMBER")
# elif month== 12:
#     print("MONTH: DECEMBER")
# else:
#     print("ERROR: \nENTER A VALID NUMBER FROM 1 to 12")
# 6
# x=5
# x+=3                              
# print(f"The value of x+=3: {x}")

# 7
# number=int(input("Enter a number: "))

# if number>1:                            #prime numbers are number greater than 1
#     for n in range(2,number):           #in range the end value is not taken
#         if number%n==0:                 
#             print(F"{number} is not a PRIME NUMBER.")
#         else:
#             print(F"{number} is a PRIME NUMBER.")
#         break                           #no break funtion then the next print will also be printed
# else:
#     print(F"{number} is not a PRIME NUMBER.")


# 8
# marks=int(input("Enter the marks: "))
# if marks>=0 and marks<=100:
#     if marks>=0 and marks<25:                 #assuming just one subject #for more subjects a percentage is calculated 
#         print("GRADE: F")
#     elif marks>=25 and marks<45:
#         print("GRADE: E")
#     elif marks>=45 and marks<50:
#         print("GRADE: D")
#     elif marks>=50 and marks<60:
#         print("GRADE: C")
#     elif marks>=60 and marks<80:
#         print("GRADE: B")
#     else:
#         print("GRADE: A")
# else:
#     print("Enter a valid marks.")


# 9

# age1= int(input("Enter first age: "))
# age2= int(input("Enter second age: "))
# age3=int(input("Enter third age: "))
# if age1>age2 and age1>age3:
#     print(f"The oldest age is {age1}")
# elif age2>age1 and age2>age3:
#     print(f"The oldest age is {age2}")
# else:
#     print(f"The oldest age is {age3}")

# if age1<age2 and age1<age3:
#     print(f"The youngest age is {age1}")
# elif age2<age1 and age2<age3:
#     print(f"The youngest age is {age2}")
# else:
#     print(f"The youngest age is {age3}")




# 10
# age=int(input("Enter your age: "))
# if age>=18:
#     print("You are ELIGIBLE to vote.")
# elif age<18 and age>0:
#     print("You are INELIGIBLE to vote.")
# else:
#     print("Enter a valid positive age.")



# 11



# number=int(input("Enter a number: "))

# if number%2==0:
#     print("The input numer is EVEN.")
# else:
#     print("The input number is ODD.")



# 12

# number= int(input("Enter a number: "))
# divide7= number%7
# if divide7==0:
#     print("DIVISIBLE BY 7: YES ")
# else:
#     print("DIVISIBLE BY 7: NO ")


# 13
# number= int(input("Enter a number: "))
# divide5= number%5
# if divide5==0:
#     print("HELLO")              #multiple of 5 is same as divisible of 5
# else:
#     print("BYE")

# 14

# percent=int(input("Enter the percentage: "))        #assmuing input is percent as iasked in question, if marks then input marks and calculate percent
# if percent>=0 and percent<=100:
#     if percent>90:
#         print("Grade: A")
#     elif percent>80 and percent<=90:
#         print("Grade: B")
#     elif percent>60 and percent<=80:
#         print("Grade: C")
#     else:
#         print("GRADE: D")
# else:
#     print("Enter a valid percentage." )

# 15

# print('''
# INDEX:  CITY
# 1   :   Delhi
# 2   :   Agra
# 3   :   Jaipur''')
# city=int(input("Enter the corresponding Index of the city: "))
# if city==1:
#     print("MONUMENT: RED FORT")
# elif city==2:
#     print("MONUMENT: TAJ MAHAL")
# elif city==3:
#     print("MONUMENT: JAL MAHAL")
# else:
#     print("Enter among the given Index")

# 16
# OUTPUT: Hello             #assuming only OUTPUT is to be answered. The code remains the sameas in questiion



# a=int(input("Enter a number: "))         
# if (a > 5 and a <=10):    
#     print("Hello")    
# else:    
#     print("Bye")

# 17


# number=int(input("Enter a number: "))
# divide_2= number%2
# divide_3= number%3

# if divide_2==0 and divide_3==0:
#     print(f'The number {number} is divisible by both 2 and 3.')
# else:
#     print(f"The number {number} is not divisible by both 2 and 3")

# 18
# print("VOWEL Identifier")
# alphabet=input("Enter a alphabet: ")
# format_alphabet=alphabet.upper()

# if format_alphabet == "A":
#     print(f"{alphabet} is a vowel") 
# elif format_alphabet == "E":
#     print(f"{alphabet} is a vowel") 
# elif format_alphabet == "I":
#     print(f"{alphabet} is a vowel") 
# elif format_alphabet == "O":
#     print(f"{alphabet} is a vowel") 
# elif format_alphabet == "U":
#     print(f"{alphabet} is a vowel") 
# else:
#     print(f"{alphabet} is a consonant") 

# 19
# num1=int(input("Enter a first number: "))
# num2=int(input("Enter a second number: "))

# print('''
# OPERATION       :   OPERATER
# ADDITION        :   +
# DIFFERENCE      :   -
# MULTIPHICATION  :   *
# DIVISION        :   /
# REMAINDER       :   %
# FLOAT           :   //''')
# print()                                                  # empty line
# operater=input("Enter the operater for the respective operation: ")
# if operater== "+" or operater=="-" or operater=="*" or operater=="/" or operater=="%" or operater=="//":
#     if operater=="+":
#         print("ADDITION: ", num1+num2)
#     elif operater=="-":
#         print ("DIFFERENCE: ", num1-num2)
#     elif operater=="*":
#         print ("MULTIPLICATION: ", num1*num2)
#     elif operater=="/":                     #no need to specify num2 to be positive. python does it automatically
#         decimal_divide=num1/num2
#         format_decimal_divide="{:.2}".format(decimal_divide)
#         print ("DIVISION: ", format_decimal_divide)
#     elif operater=="%":
#         print ("REMAINDER: ", num1%num2)
#     else:
#         print("FLOAT: ",num1//num2)
# else:
#     print("ERROR!!! \nThe operator is INVALID")