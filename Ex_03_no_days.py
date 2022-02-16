# Create a program using maths and f-strings that tell us how many days, weeks and months we have left if we lived until 90 years old.

# Solution: 

age = int(input("What is your current age?"))

years_remaining = 90 - age # 90 - ages gives the years remaining
days_remaning = years_remaining * 365 # 365 days in a year
weeks_remaning = years_remaining * 52 # 52 weeks 
months_remaning = years_remaining * 12 # 12 months

print(f"You have {days_remaning} days, {weeks_remaning} weeks, and {months_remaning} months left.")

