def main():
    grocery_list = {}

    try:
        while True:
            item = input("Enter an item: ").strip().upper()
            
            if not item:
                continue
            
            if item.isdigit():
                print("Error: Numbers are not allowed as items.")
                continue
            
            if item in grocery_list:
                grocery_list[item] += 1  
            else:
                grocery_list[item] = 1  

    except KeyboardInterrupt:
        # Handle Ctrl+C and display the grocery list
        print("\nGrocery List:")
        for item, count in sorted(grocery_list.items()):  # Sort items alphabetically
            print(f"{count} {item}")

if __name__ == "__main__":
    main()