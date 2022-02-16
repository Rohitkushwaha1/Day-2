# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# Solution:

height = int(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

BMI = (weight/height**2)  #another way--> BMI = (weight/height*height)
BMI_as_int = int(BMI)

print((BMI_as_int))