def main():
    c = 300000000; # Speed of light in m/s
    try:
        m = int(input("m:"));
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    E = m * c**2;
    print(E);

main()