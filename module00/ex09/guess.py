from random import randint
from collections import namedtuple

Phrases = namedtuple('Phrases', 'high low win')
RETURN_VALUES = Phrases("Too high!", "Too low!", "You won!")


def start_message():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

def check_guess(correct_number: int, guessed_number: int):
    if correct_number > guessed_number:
        return RETURN_VALUES.low
    elif correct_number < guessed_number:
        return RETURN_VALUES.high
    else:
        return RETURN_VALUES.win

def game_loop():
    guesses = 0
    rand_number = randint(1, 99)

    start_message()
    while True:
        guess = input("What's your guess between 1 and 99?\n>> ")
        if guess == "exit":
            exit()
        guesses += 1
        try:
            guess = int(guess)
        except:
            print("Not a number.")
            continue
        print(check_guess(rand_number, guess))
        if rand_number == guess and rand_number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if rand_number == guess and guesses == 1:
            print("You won in the first try!")
            break
        elif rand_number == guess:
            print(f"You won in {guesses} guesses!")
            break
        
def main():
    game_loop()

if __name__ == '__main__':
    main()
