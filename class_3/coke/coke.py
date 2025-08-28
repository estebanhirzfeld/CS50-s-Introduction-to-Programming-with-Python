def main():
    balance = 0
    while balance < 50:
        try:
            coin = int(input("Insert coin (10, 25, 50): "))
            
            if coin not in [10, 25, 50]:
                print("Invalid coin. Remaining: 50")
            else:
                balance += coin
                if balance < 50:
                    print(f"Remaining: {50 - balance}")
        except ValueError:
            print("Invalid input. Please insert a valid coin.")
    
    print("Coke dispensed!")

main();