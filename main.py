import random

def generate_word(word_list):
    return random.choice(word_list)

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

def play_game(difficulty, word_list):
    word = generate_word(word_list)
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

def display_statistics(total_games, wins, difficulty):
    win_rate = wins / total_games * 100 if total_games > 0 else 0
    print(f"\nGame Stats:")
    print(f"Total games: {total_games}")
    print(f"Games won: {wins}")
    print(f"Win rate: {win_rate:.2f}%")
    print(f"Current difficulty: {difficulty.capitalize()}")

def update_leaderboard(player_name, score, leaderboard):
    if player_name not in leaderboard or score > leaderboard[player_name]:
        leaderboard[player_name] = score

def display_leaderboard(leaderboard):
    if leaderboard:
        print("\nLeaderboard:")
        for player, score in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True):
            print(f"{player}: {score}")
    else:
        print("\nNo leaderboard data available.")

def add_custom_word(word_list):
    new_word = input("Enter a new palindrome to add: ").lower()
    if is_palindrome(new_word) and new_word.isalpha():
        word_list.append(new_word)
        print(f"{new_word} has been added to the word list.")
    else:
        print("The word must be a valid palindrome and contain only letters.")

def select_difficulty():
    return validate_input("Select difficulty (easy/medium/hard): ", ['easy', 'medium', 'hard'])

def main():
    # Initial word list
    word_list = ["racecar", "level", "rotor", "madam", "kayak", "deified", "civic", "stats", "noon", "refer"]
    leaderboard = {}
    player_name = get_player_name()
    score = 0
    total_games = 0
    wins = 0

    display_instructions()

    while True:
        difficulty = select_difficulty()
        max_guesses = {'easy': 7, 'medium': 5, 'hard': 3}[difficulty]
        total_games += 1

        if play_game(difficulty, word_list):
            score += 1
            wins += 1
            update_leaderboard(player_name, score, leaderboard)

        display_score(player_name, score)
        display_statistics(total_games, wins, difficulty)

        action = validate_input("Would you like to add a custom word, view the leaderboard, or play again? (add/leaderboard/play): ", ['add', 'leaderboard', 'play'])
        if action == 'add':
            add_custom_word(word_list)
        elif action == 'leaderboard':
            display_leaderboard(leaderboard)

        if not play_again():
            break

    print(f"\nThank you for playing, {player_name}! here i a summary of your game:")
    display_statistics(total_games, wins, difficulty)
    print(f"Your final score is: {score}")
    print("Goodbye and have a great day!")

if __name__ == "__main__":
    main()
