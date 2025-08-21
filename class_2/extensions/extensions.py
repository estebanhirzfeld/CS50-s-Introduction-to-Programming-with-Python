def main():
    user_input = input("Enter file name: ")

    user_input_extension = user_input.strip().lower().split('.')[-1]

    print(f"File extension: {user_input_extension}")

    if user_input_extension in ['gif', 'jpg', 'jpeg', 'png']:
        print(f"image/{user_input_extension}")
    elif user_input_extension in ['txt', 'pdf']:
        print("text/plain")
    elif user_input_extension == 'zip':
        print("application/zip")
    else:
        print("Unknown file type")

main()