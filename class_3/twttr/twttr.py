def main():
    vowels = ['a', 'e', 'i', 'o', 'u']

    user_input = input("Enter a string: ")
    
    result = []
    for char in user_input:
        if char.lower() not in vowels:
            result.append(char)
    
    print("".join(result))

main()