import random
import time
import os

randomNumber = ""

#Initialize the game with the proper greetings and number choice
def init():
    quotes = ["Hello there stranger...",
    "Welcome to the guessing game!",
    "I've picked a random number between 1 and 6, can you guess which it was?"]
    randomNumber = random.randint(1,6)
    for quote in quotes:
        print(quote)
        time.sleep(0.75)
    return randomNumber
#Return the proper tip depending on higher or lower number
def highOrLow(x, y):
    if x > y:
        return "Try a little lower, stranger..."
    elif x < y:
        return "Try a little higher, stranger..."
#Insert the tip in the middle of the quotes depending if higher or lower number and asks if player wants to quit?
def tryAgain(x, y):
    quotes = ["Oh sorry, that's not it...",
    "Or type 'exit' to give up..."]
    quotes.insert(1, highOrLow(x, y))
    for quote in quotes:
        print(quote)
        time.sleep(0.75)
    newGuess = input("Your new guess: ")
    return newGuess
#Congratulates if the player has guessit correctly
def youWon():
    quotes = ["I can't believe it...",
    "You've actually guessed it!",
    "Congratulations stranger, you've won!"]
    for quote in quotes:
        print(quote)
        time.sleep(0.75)


def main():
    randomNumber = init()
    guess = int(input("Your guess: "))
    while guess != randomNumber:
        guess = tryAgain(guess, randomNumber)
        if guess.lower() == "exit":
            print("You've died...")
            print(f"And the number was {randomNumber}, hahaHAHAHA!!!")
            break
        guess = int(guess)
    if guess == randomNumber:
        youWon()

if __name__ == "__main__":
    main()