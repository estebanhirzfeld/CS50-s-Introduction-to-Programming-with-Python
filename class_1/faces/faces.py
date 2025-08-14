def main():
    text = input("")
    text = text.lower().replace("hello", "hello 😃")
    text = text.lower().replace("goodbye", "goodbye 😔")
    text = text.title()
    print(text)

main()