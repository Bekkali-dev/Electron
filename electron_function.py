from datetime import date

def calculate_age_from_year(year):
    current_year = date.today().year
    return current_year - year

def calculate_age():
    year = int(input("Enter the year you were Born: "))
    age = calculate_age_from_year(year)
    print(f"Your age is {age} yearssssssss")

calculate_age()
