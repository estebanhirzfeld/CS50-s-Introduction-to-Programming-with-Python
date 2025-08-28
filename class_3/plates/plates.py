def main():
    plate = input("Enter a vanity plate: ")
    
    if not (2 <= len(plate) <= 6 and plate[-1].isdigit()):
        print("Invalid plate: Must be 2-6 characters long and end with a number.")
        return
    
    if not plate.isalnum(): #ALPHANUMERIC CHECK
        print("Invalid plate: Must not contain spaces, punctuation, or special characters.")
        return
    
    print("Valid plate:", plate.upper())

main();