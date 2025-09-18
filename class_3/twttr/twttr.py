def main():
    user_input = input("Enter a string: ")
    print(remove_vowels(user_input))


def remove_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_str:
        if char.lower() not in vowels:
            result.append(char)
    return ''.join(result)


if __name__ == "__main__":
    main()