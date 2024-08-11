import random

def generate_word():
    # Random words for the game (palindromes)
    words = ["racecar", "level", "rotor", "madam", "kayak", "deified", "civic", "stats", "noon", "refer"]
    return random.choice(words)

def get_guess():
    # Get the player's guess
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) == 1:
            return guess
        else:
            print("Please enter only one letter.")

def check_guess(guess, word):
    # Check and return a message
    if guess in word:
        return f"Good guess! {guess} is in the word."
    else:
        return f"Sorry, {guess} is not in the word."

def is_palindrome(word):
    # Check if the word is a palindrome
    return word == word[::-1]

def play_game():
    # Play the palindrome game
    word = generate_word()
    guesses = []
    max_guesses = 5
    print(f"The word is {len(word)} letters long.")
    print("Hint: It's a palindrome!")  # Added hint
    while len(guesses) < max_guesses:
        guess = get_guess()
        if guess in guesses:
            print("You already guessed that letter. Try again.")
        else:
            guesses.append(guess)
            print(check_guess(guess, word))
            if guess in word:
                if set(guess) == set(word):
                    print(f"Congratulations! You guessed the word: {word}.")
                    break
                else:
                    # Check if the guessed letters form a palindrome
                    guessed_letters = "".join(sorted(guesses))
                    if is_palindrome(guessed_letters):
                        print("You've guessed a palindrome!")
    if len(guesses) == max_guesses:
        print(f"Sorry, you ran out of guesses! The word was {word}")

def get_player_name():
    # Get the player's name
    name = input("Enter your name: ")
    return name

def display_score(player_name, score):
    # Show the player's score
    print(f"{player_name}, your score is: {score}")

def play_again():
    # Ask if the player wants to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ('y', 'n'):
            return play_again == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n.'")
            
#More added functions
def validate_input(input_str, valid_options):
    # Validate the input
    while True:
        user_input = input(input_str).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid, Try again.")

def display_instructions():
    #Show the instructions
    print("Welcome to the Palindrome Checker game!")
    print("Guess the letters to reveal the palindrome.")
    print("You have a limited number of guesses!")

def save_high_score(player_name, score):
    player_name = player_name 
    score = score
    score = 0 
    if player_name == "":
        print("The Value of the name cannot be empty!")
        
    else:
        print(f"User:{player_name}")
    pass
    
def main():
    # The main function
    player_name = get_player_name()
    score = 0
    while True:
        play_game()
        score += 1
        display_score(player_name, score)
        if not play_again():
            break

if __name__ == "__main__":
    main()
