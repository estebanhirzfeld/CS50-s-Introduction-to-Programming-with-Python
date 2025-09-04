def main():
    try:
        fraction = input("Enter a fraction (x/y): ").strip()
        
        if len(fraction) != 3 or '/' not in fraction:
            raise ValueError("Input must be in the format x/y")
        
        x, y = map(int, fraction.split('/'))
        
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        
        result = x / y
        
        if result == 0:
            print("E")
        elif result == 1:
            print("F")
        else:
            print(f"{int(result * 100)}%")
    
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

main();