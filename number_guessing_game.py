import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    lower_limit = int(input("Enter the lower limit for the range: "))
    upper_limit = int(input("Enter the upper limit for the range: "))
    number_to_guess = random.randint(lower_limit, upper_limit)
    attempts = 0

    while True:
        guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts!")
            break

    return attempts

def main():
    best_score = float('inf')
    while True:
        attempts = play_game()
        print(f"Your score for this game: {attempts} attempts")
        if attempts < best_score:
            best_score = attempts
            print("New high score!")
        
        # Add an anchor text with a website link
        website_link = "https://www.proinstaapks.com"
        print(f"For more fun, visit our website: {website_link}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Your best score: {best_score} attempts")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
