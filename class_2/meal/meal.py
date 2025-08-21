def main():
    # brakfast = before range: 6:00 - 10:00
    # lunch = before range: 11:00 - 15:00
    # dinner = before range: 17:00 - 21:00

    user_input = input("Enter the time in HH:MM format: ")
    user_input = user_input.strip().split(":")

    if len(user_input) != 2:
        print("Invalid input. Please enter the time in HH:MM format.")
        return
    else:
        hour = int(user_input[0])
        minute = int(user_input[1])

        if hour < 0 or hour > 23:
            print("Invalid hour. Please enter a valid hour between 0 and 23.")
            return

        if minute < 0 or minute > 59:
            print("Invalid minute. Please enter a valid minute between 0 and 59.")
            return

    if 6 <= hour < 10 or (hour == 10 and minute == 0):
        print("It's breakfast time!")
    elif 11 <= hour < 15 or (hour == 15 and minute == 0):
        print("It's lunch time!")
    elif 17 <= hour < 21 or (hour == 21 and minute == 0):
        print("It's dinner time!")
    else:
        print("It's not meal time!")

main();



    