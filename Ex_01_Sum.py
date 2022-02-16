# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Solution:

Two_Digit_Number = (input("Enter Two digit number: ")) # The user enter the two digit number of string data type

# We convert string data type to integer data type so that we can add them to produce a sum of first and the last digit(i.e. second digit)
First_digit = int(Two_Digit_Number[0]) 
Second_digit =int(Two_Digit_Number[1]) 

result = First_digit + Second_digit

print("The sum of first digit and second digit is :", result)