import random

def generate_word():
    #random words of palindrome for the game
    words = ["racecar", "level", "rotor", "madam", "kayak", "deified", "civic", "stats", "noon", "refer"]
    return random.choice(words)

def get_guess():
    #get the guess
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) == 1:
            return guess
        else:
            print("Please enter only one letter.")

def check_guess(guess, word):
    #check and return a message
    if guess in word:
        return f"Good guess! {guess} is in the word."
    else:
        return f"Sorry, {guess} is not in the word."

def is_palindrome(word):
   #check if word is palindrome
    return word == word[::-1]

def play_game():
    #if you want to play the palindrome game again
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
    #get the player name
    name = input("Enter your name: ")
    return name

def display_score(player_name, score):
    #show score of user
    print(f"{player_name}, your score is: {score}")

def play_again():
    #if player wants to go again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ('y', 'n'):
            return play_again == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    #the main function
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
