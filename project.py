import random

def game():
    num = random.randint(1, 100)
    guesses = 1
    guessed_num = 0
    while(guessed_num != num):
        guessed_num = get_guess()
        if(num == guessed_num):
            print("Correct!")
            print("Congratulations, You won in "+ str(guesses) + " attempts")
        elif(num > guessed_num): # type: ignore
            print("Too Low")
            guesses += 1
        else:
            print("Too high")
            guesses += 1

    return None

def get_guess():
    guess = 0
    while(True): # type: ignore
        try:
            guess = int(input("What is your guess: "))
            if(guess < 1 or guess > 100): # type: ignore
                guess = ""
                print("Please enter a valid number (must be int from 1 to 100).")
            else:
                return guess
        except ValueError:
            print("Please enter a valid number (must be int from 1 to 100).")

def run_tests():
    game()
    
if __name__ == "__main__":
    run_tests()