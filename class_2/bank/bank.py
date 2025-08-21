def main():

    balance = 0.0;

    user_input = input("Greeting:");
    user_input = user_input.strip().lower();

    if user_input.startswith("h") and not user_input.startswith("hello"):
        balance=+ 20;       
    elif user_input.startswith("hello") or user_input.startswith(""):
        pass
    else:
        balance=+100;

    print(f"${balance:.2f}");

main()
    
        
