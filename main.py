import random

def generate_word():
    words = ["racecar", "level", "rotor", "madam", "kayak", "deified", "civic", "stats", "noon", "refer"]
    return random.choice(words)

def get_guess():
    while True:
        
        guess = input("Enter your guess: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter only one letter.")

def check_guess(guess, word):
    if guess in word:
        return f"Good guess! {guess} is in the word."
    else:
        return f"Sorry, {guess} is not in the word."

def is_palindrome(word):
    return word == word[::-1]

def play_game(difficulty):
    
    word = generate_word()
    word_set = set(word)
    guesses = []
    max_guesses = {'easy': 7, 'medium': 5, 'hard': 3}[difficulty]
    print(f"\nDifficulty: {difficulty.capitalize()}")
    print(f"The word is {len(word)} letters long.")
    print("Hint: It's a palindrome!")

    while len(guesses) < max_guesses:
        guess = get_guess()
        if guess in guesses:
            print("You already guessed that letter. Try again.")
        else:
            guesses.append(guess)
            print(check_guess(guess, word))

            guessed_letters = set(guesses)
            if guessed_letters == word_set:
                
                print(f"Congratulations! You guessed the word: {word}.")
                return True

            guessed_letters_str = "".join(sorted(guesses))
            if is_palindrome(guessed_letters_str):
                print("You've guessed a palindrome!")

            if difficulty == 'hard' and len(guesses) == max_guesses - 2:
                
                print("Warning: You're close to running out of guesses!")
            if difficulty == 'medium' and len(guesses) == max_guesses - 3:
                
                print("Hint: You're getting closer!")

    print(f"Sorry, you ran out of guesses! The word was {word}")
    return False

def get_player_name():
    return input("Enter your name: ").strip()

def display_score(player_name, score):
    print(f"\n{player_name}, your score is: {score}")

def play_again():
    return validate_input("Do you want to play again? (y/n): ", ['y', 'n']) == 'y'

def validate_input(input_str, valid_options):
    while True:
        
        user_input = input(input_str).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of {', '.join(valid_options)}.")

def display_instructions():
    
    print("\nWelcome to the Palindrome Checker!")
    print("Guess the letters to reveal the palindrome.")
    print("You have a limited number of guesses!")
    
    print("Try to guess all letters correctly within the allowed number of guesses.")
    print("If you get stuck, you can get a hint!")

def display_statistics(total_games, wins, max_guesses, difficulty):
    
    win_rate = wins / total_games * 100 if total_games > 0 else 0

    print(f"\nGame Statistics:")
    print(f"Total games played: {total_games}")
    
    print(f"Games won: {wins}")
    print(f"Win rate: {win_rate:.2f}%")
    
    print(f"Current difficulty: {difficulty.capitalize()}")
    print(f"Max guesses allowed: {max_guesses}")


def select_difficulty():
    return validate_input("Select difficulty (easy/medium/hard): ", ['easy', 'medium', 'hard'])


def main():
    
    display_instructions()
    player_name = get_player_name()
    score = 0
    total_games = 0
    wins = 0

    while True:
        
        difficulty = select_difficulty()
        max_guesses = {'easy': 7, 'medium': 5, 'hard': 3}[difficulty]
        total_games += 1
        
        if play_game(difficulty):
            score += 1
            wins += 1

        display_score(player_name, score)
        display_statistics(total_games, wins, max_guesses, difficulty)
      

        if not play_again():
            
            print(f"\nThank you for playing, {player_name}! Goodbye!")
            break

if __name__ == "__main__":
    main()
