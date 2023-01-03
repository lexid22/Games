import random

def number_guess():
    randomNumber = random.randrange(0,100)
    tries = 5

    print("I’m thinking of a number in the range 0-100. You have five tries to guess it.")
    guessed = False

    while guessed == False:
        userInput = (input(f"You have {tries} tries left. Next Guess: "))
        while not userInput.isdigit():
            print("That is not a number. Please enter a number. ")
            userInput = (input(f"You have {tries} tries left. Next Guess: "))
        userInput = int(userInput)
        tries -= 1
        if tries == 0:
            print("Your guess is incorrect. The right answer is " + str(randomNumber))
            break
        if userInput == randomNumber:
            guessed = True
            print("You are right! I was thinking of " + str(randomNumber) + "!")
        elif userInput>randomNumber:
            print(str(userInput) + " is too high.")
        elif userInput < randomNumber:
            print(str(userInput) + " is too low.")

    print("End of game")
