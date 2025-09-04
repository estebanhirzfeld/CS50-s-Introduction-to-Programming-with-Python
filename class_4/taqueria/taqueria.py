menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    
    while True:
        try:
            item = input("Item: ").strip().title()
            if item == "":
                break
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
            else:
                print("Item not found in menu.")
        except EOFError: # Handle EOF (End Of File)
            break
        except KeyboardInterrupt: # Handle Ctrl+C interruption
            print("\nExiting...")
            break
    print(f"Final Total: ${total:.2f}")

main();