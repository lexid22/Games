
def hangman():
    word = "Secret"

    tries = 5
    guesses = []
    done = False

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end = " ")
            else:
                print("_", end = " ")
        print("")

        guess = input(f"You have {tries} tries left. Next Guess: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            tries -= 1
            if tries == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done:
        print("You found the word!")
    else:
        print(f"Game over! The word was {word} ")
