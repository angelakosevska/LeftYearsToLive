
age = input("What is your current age? ")

#1 year=365 days 
#1 year= 52 weeks 
#1 year=12 months
#max expected years to live
years=90
left_years=90-int(age)

days=left_years * 365
weeks= left_years * 52
months = left_years * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
