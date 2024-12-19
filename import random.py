import random

def guessing_game():
    while True:
        # Generate a random number between 1 and 10
        number_to_guess = random.randint(1, 10)
        attempts = 0

        print("Welcome to the Guessing Number Game!")
        print("I have selected a number between 1 and 10. Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Try again! Your guess is too low.")
                elif guess > number_to_guess:
                    print("Try again! Your guess is too high.")
                else:
                    print(f"Yeah, you guessed it! The number was {number_to_guess}.")
                    print(f"It took you {attempts} attempts.")
                    break

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue

        # Prompt to play again or quit
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing the guessing game!")
            break

# Run the guessing number game
guessing_game()