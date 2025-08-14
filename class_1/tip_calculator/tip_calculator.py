def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.strip().replace("$", "").replace(",", ".");
    try:
        d = float(d)
    except ValueError:
        print("Invalid input. Please enter a valid dollar amount.")
        return 0.0
    return d
def percent_to_float(p):
    p = p.strip().replace("%", "");
    try:
        p = float(p)
    except ValueError:
        print("Invalid input. Please enter a valid percentage.")
        return 0.0
    if p < 0 or p > 100:
        print("Percentage must be between 0 and 100.")
        return 0.0
    p = p / 100.0

main()
