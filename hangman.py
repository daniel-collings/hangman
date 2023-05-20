# Pseudo Instructions - to guide development only 
# array of words
# upto 5 incorrect guesses
# take user input
# hide letters with *
# show letters correctly guessed
# show list of guessed letters
# show how many guesses remain

from random import randint

word_bank = ["Middlesbrough", "Hartlepool"]

def start_new_game():
    guesses_remaining = 5
    guesses = {"",}
    hangman_word = get_hangman_word()
    game_in_play(hangman_word, guesses_remaining, guesses)

def get_hangman_word():
    cap = word_bank[randint(0,(len(word_bank)-1))].upper()
    return cap

def game_in_play(hangman_word, guesses_remaining, guesses):
    while True:
        print(f"\n\t==========\nChances remaining: {guesses_remaining}")
        if(not guesses_remaining):
            print("\nNo Chances Remaining - GAME OVER!\n\t==========\n")
            break

        print("\nEnter a single letter:")
        guess = input()
        guess = guess.upper()

        if guess in guesses:
            print(f"Oops! You've used '{guess}' already. Try again (no pts deducted).")
            continue
        elif len(guess) > 1 or not(guess.isalpha()):
            print("Oops! I only accept a single valid alphabetic character.\n\nTry again.\n")
            continue
        elif guess not in guesses:
            guesses.add(guess)
            word = masked_word(hangman_word, guesses)            
            
            if(guess not in hangman_word):
                guesses_remaining -= 1
                continue

            if("*" not in word):
                print(f"\n\t==========\nCongrats! You've smashed it. The word is: {word}\n\n")
                break
            else:
                print(f"\n\nWell done! You're getting closer and the current masked word is: {word}\n")
        else:
            print("Oops! I only accept a single valid alphabetic character.\n\nTry again.\n")

def masked_word(word, guesses):
    masked = ""
    for character in word:
        if({character} & guesses):
            masked += character
        else:
            masked += "*"
    return masked

start_new_game()