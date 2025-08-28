def main():
    user_input = input("Enter a string: ")
    result = []
    for char in user_input:
        if char.isupper():
            result.append("_" + char.lower())
        else:
            result.append(char)
    print("".join(result))

main();