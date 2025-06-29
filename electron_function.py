from datetime import date
def age():
    current_year = date.today().year
    year=int(input("Enter the year you were Born: "))
    calculation= current_year - year
    print(f"Your age is {calculation} years")

age()