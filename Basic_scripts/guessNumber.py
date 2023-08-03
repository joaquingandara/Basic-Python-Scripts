from numpy import random

def game():
    print("Guess the number between 1 to 10\n")
    randomNumber = random.randint(1,10)
    numOfGuesses = 3 
    userGuess = 0
    while numOfGuesses != 0 and userGuess != randomNumber:
        userGuess = int(input("Enter a number\n"))
        numOfGuesses-=1
    if userGuess == randomNumber: 
        print("Correct")
    else:
        print("Game over")

if __name__ == "__main__":
    game()