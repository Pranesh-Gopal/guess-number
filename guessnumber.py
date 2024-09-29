import random

# Function to generate a random number
def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

# Function to get the player's guess and handle input errors
def get_player_guess():
    try:
        return int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        return get_player_guess()

# Function to provide hints to the player
def provide_hint(player_guess, target_number):
    if player_guess < target_number:
        return "Too low!"
    elif player_guess > target_number:
        return "Too high!"
    else:
        return "Correct!"

# Main game loop
def play_game():
    # Random number between 1 and 100
    target_number = generate_random_number(1, 100)
    attempts = 10  # Updated to 10 attempts
    
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        guess = get_player_guess()  # Get player's guess
        feedback = provide_hint(guess, target_number)  # Provide feedback
        print(feedback)
        
        if feedback == "Correct!":
            print("Congratulations! You've guessed the number.")
            break
        
        attempts -= 1  # Decrease the number of attempts after each guess
    
    if attempts == 0:
        print(f"\nSorry, you've run out of attempts! The number was {target_number}.")
    print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
