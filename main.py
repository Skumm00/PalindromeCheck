import random
import os

def generate_word():
    # Random words for the game (palindromes)
    words = ["racecar", "level", "rotor", "madam", "kayak", "deified", "civic", "stats", "noon", "refer"]
    return random.choice(words)

def get_guess():
    # Get the player's guess
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) == 1 and guess.isalpha():
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
    word_set = set(word)  # To keep track of unique letters in the word
    guesses = []
    max_guesses = 5
    print(f"The word is {len(word)} letters long.")
    print("Hint: It's a palindrome!")

    while len(guesses) < max_guesses:
        guess = get_guess()
        if guess in guesses:
            print("You already guessed that letter. Try again.")
        else:
            guesses.append(guess)
            print(check_guess(guess, word))

            # Display guessed letters
            guessed_letters = set(guesses)
            if guessed_letters == word_set:
                print(f"Congratulations! You guessed the word: {word}.")
                return True  # Game won

            # Check if the guessed letters form a palindrome
            guessed_letters_str = "".join(sorted(guesses))
            if is_palindrome(guessed_letters_str):
                print("You've guessed a palindrome!")

    print(f"Sorry, you ran out of guesses! The word was {word}")
    return False  # Game lost

def get_player_name():
    # Get the player's name
    name = input("Enter your name: ").strip()
    return name

def display_score(player_name, score):
    # Show the player's score
    print(f"{player_name}, your score is: {score}")

def play_again():
    # Ask if the player wants to play again
    return validate_input("Do you want to play again? (y/n): ", ['y', 'n']) == 'y'

def validate_input(input_str, valid_options):
    # Validate the input
    while True:
        user_input = input(input_str).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of {', '.join(valid_options)}.")

def display_instructions():
    # Show the instructions
    print("Welcome to the Palindrome Checker game!")
    print("Guess the letters to reveal the palindrome.")
    print("You have a limited number of guesses!")
    print("Try to guess all letters correctly within the allowed number of guesses.")
    print("If you get stuck, you can get a hint!")

def save_high_score(player_name, score):
    # Save the high score
    if player_name:
        with open('high_scores.txt', 'a') as file:
            file.write(f"{player_name}: {score}\n")
        print(f"High score saved for {player_name}: {score}")
    else:
        print("The value of the name cannot be empty!")

def update_leaderboard(player_name, score):
    # Update leaderboard with new high scores
    leaderboard = []
    if os.path.exists('high_scores.txt'):
        with open('high_scores.txt', 'r') as file:
            leaderboard = [line.strip() for line in file]

    leaderboard.append(f"{player_name}: {score}")
    leaderboard.sort(key=lambda x: int(x.split(': ')[1]), reverse=True)

    with open('high_scores.txt', 'w') as file:
        for entry in leaderboard[:10]:  # Keep only the top 10 scores
            file.write(f"{entry}\n")
    print("Leaderboard updated!")

def give_hint(word, guesses):
    # Provide a hint by revealing one of the letters not yet guessed
    remaining_letters = set(word) - set(guesses)
    if remaining_letters:
        hint_letter = random.choice(list(remaining_letters))
        print(f"Hint: One of the remaining letters is '{hint_letter}'.")
    else:
        print("No more hints available.")

def display_statistics(total_games, wins):
    # Display game statistics
    print(f"\nGame Statistics:")
    print(f"Total games played: {total_games}")
    print(f"Games won: {wins}")
    print(f"Win rate: {wins / total_games * 100:.2f}%")

def main():
    # The main function
    display_instructions()
    player_name = get_player_name()
    score = 0
    total_games = 0
    wins = 0

    while True:
        total_games += 1
        if play_game():
            score += 1
            wins += 1
            update_leaderboard(player_name, score)
        else:
            update_leaderboard(player_name, score)

        display_score(player_name, score)
        display_statistics(total_games, wins)
        if not play_again():
            break

if __name__ == "__main__":
    main()
