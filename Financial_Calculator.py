import math

def annuity_monthly_growth():
    P = float(input("Enter the principal amount in € (P): "))
    r = float(input("Enter the monthly interest rate (r): "))
    t = float(input("Enter the time in months (t): "))
    
    annuity = P * (1 + r) ** t
    print("Annuity =", annuity)

def calculate_annuity_continuous_growth():
    P = float(input("Enter the principal amount in € (P): "))
    r = float(input("Enter the annual interest rate (as a decimal): "))
    t = float(input("Enter the time in years (t): "))
    n = int(input("Enter the number of times interest is compounded per year (n): "))
    
    # Calculate the annuity with continuous growth
    annuity = P * (1 + (r / n)) ** (n * t)
    
    print("Annuity =", annuity)

def calculate_monthly_mortgage_payment():
    P = float(input("Amount borrowed in € (principal): "))
    r = float(input("Annual percentage rate: "))
    t = float(input("Number of years: "))
    # numerator
    n = (r/12)*(1+r/12)**(12*t)
    # denominator
    d = (1+r/12)**(12*t)-1
    pmt = P*n/d
    print("Monthly payment =", pmt,"€")

def estimate_retirement_investment_balance():
    p = float(input("Enter the principal amount in € (p): "))
    r = float(input("Enter the annual interest rate (as a decimal, r): "))
    t = int(input("Enter the number of years (t): "))
    monthly = float(input("Enter the monthly contribution amount in €: "))

    annuity = p

    for a in range(12 * t):
        annuity = (annuity + monthly) * (1 + (r / 12))

    annuity_value = round(annuity, 2)
    annual_income = round(annuity * r, 2)

    print("Annuity value =", annuity_value,"€")
    print("Annual income from interest =", annual_income,"€")

def determine_time_to_double():
    principal = float(input("Enter the initial amount in €: "))
    annual_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
    
    if annual_rate <= 0:
        raise ValueError("Annual rate must be greater than 0")
    
    time = 0
    while principal < 2 * principal:
        principal *= (1 + annual_rate)
        time += 1
    
    print(f"It takes {time} years for the initial amount to double at the specified annual rate.")

def rate_of_growth():
    starting_value = float(input("Enter the starting value in €: "))
    ending_value = float(input("Enter the ending value in €: "))
    time = float(input("Enter the time period (in years): "))
    
    if time <= 0:
        raise ValueError("Time must be greater than 0")
    
    annual_rate = ((ending_value / starting_value) ** (1 / time)) - 1
    print(f"The rate of growth is approximately {annual_rate * 100}% per year.")

def solve_logarithmic_equations():
    # Prompt the user to input the base and result
    base = float(input("Enter the base (for e.g. 2): "))
    result = float(input("Enter the result (for e.g. 64): "))

    # Calculate the exponent using the logarithm
    exp = math.log(result, base)

    # Print the calculated exponent
    print("Exponent = ", exp)


def convert_to_scientific_notation():
    a = float(input('Enter a number to convert to scientific notation: '))

    x = math.floor(math.log10(a))
    n = round(a / 10 ** x, 2)

    print(f"{a} = {n} * 10^{x}")
    return n, x

def convert_from_scientific_notation():
    n = float(input('Enter the coefficient (n): '))
    x = int(input('Enter the exponent (x): '))

    result = n * 10 ** x
    print(f"{n} * 10^{x} = {result}")


def main():
    while True:
        print("Menu:")
        print("1. Calculate annuity with monthly growth")
        print("2. Calculate annuity with continuous growth")
        print("3. Calculate the monthly mortgage payment - given the principle, rate & time")
        print("4. Estimate retirement investment balance")
        print("5. Determine how long until an amount doubles, given the rate")
        print("6. Determine the rate of growth - given the starting value, time, & ending value")
        print("7. Solve logarithmic equations")
        print("8. Convert to scientific notation")
        print("9. Convert from scientific notation")
        print("10. Exit")

        choice = input("Enter the number of your choice (1-10): ")

        if choice == "1":
            print('You chose calculate annuity with monthly growth')
            annuity_monthly_growth()
        elif choice == "2":
            print("You chose calculate annuity with continuous growth")
            calculate_annuity_continuous_growth()
        elif choice == "3":
            print("You chose calculate the monthly mortgage payment - given the principle, rate & time")
            calculate_monthly_mortgage_payment()
        elif choice == "4":
            print("You chose estimate retirement investment balance")
            estimate_retirement_investment_balance()
        elif choice == "5":
            print("You chose determine how long until an amount doubles, given the rate")
            determine_time_to_double()
        elif choice == "6":
            print("You chose determine the rate of growth - given the starting value, time, & ending value")
            rate_of_growth()
        elif choice == "7":
            print("You chose solve logarithmic equations")
            solve_logarithmic_equations()
        elif choice == "8":
            print("You chose convert to scientific notation")
            convert_to_scientific_notation()
        elif choice == "9":
            print("You chose convert from scientific notation")
            convert_from_scientific_notation()
        elif choice == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-10).")

if __name__ == "__main__":
    main()