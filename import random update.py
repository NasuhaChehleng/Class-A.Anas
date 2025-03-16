import random

def generate_number():
    return random.randint(1, 10)  

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_game():
    number_to_guess = generate_number()
    attempts = 10
    
    print("Welcome to the Guessing Game! 🎯")
    print("I have selected a number between 1 and 10. Try to guess it!")
    
    while attempts > 0:
        print(f"Attempts remaining: {attempts}")
        guess = get_user_guess()
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
            return
        
        attempts -= 1
    
    print(f"Game over! The correct number was {number_to_guess}. Better luck next time!")

if __name__ == "__main__":
    play_game()