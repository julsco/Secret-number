import random

# Function to get user's number


def getNumber():
    while True:
        try:
            number = int(
                input("Please insert a number between 0-10 or -1 to quit: "))
            if number == -1:
                print("Thanks for playing! See you next time")
                quit()
            elif number < 0 or number > 10:
                raise ValueError
        except ValueError:
            print("Please enter a valid number")
        else:
            break
    return number


# Main While
while True:
    chances = 3  # initializing number of chances

    # getting a random number between 0 and 10
    random_number = random.randint(0, 10)
    # print(random_number)

    # Comparing user's numbers with the secret number
    while chances != 0:
        user_number = getNumber()
        if user_number == random_number:
            print("Congratulations! You have guessed the secret number!")
            break
        else:
            if user_number > random_number:
                print("Try lower")
            else:
                print("Try higher")
            chances -= 1
            print("Remainding attempts: ", chances)

# Game lost message
    if chances < 1:
        print("You have lost. Good luck next time :)")

# Play again?
    while True:
        play_again = input("To play again press \"Y\" or \"N\" to quit ")
        if play_again == "Y":
            chances = 3
            break
        elif play_again == "N":
            print("Thanks for playing! See you next time")
            quit()
        else:
            print("Please press \"Y\" to play again or \"N\" to quit")
