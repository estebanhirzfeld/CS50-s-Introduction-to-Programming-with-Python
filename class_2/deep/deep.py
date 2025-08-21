def main():
    print("What is the Answer to the great Question of Life, the Universe, and Everything?")
    answer = input("Press Enter to continue...")

    answer = answer.strip().lower().replace("  "," "); 

    match answer:
        case "42" | "forty-two" | "forty two":
            print("Correct! The answer is indeed 42.");
        case _:
            print("Incorrect. The answer is 42.");

main();