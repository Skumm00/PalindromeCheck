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

def play_game():
    #if you want to play the palindrome game again
    word = generate_word()
    guesses = []
    max_guesses = 5
    print(f"The word is {len(word)} letters long.")
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
    if len(guesses) == max_guesses:
        print(f"Sorry, you ran out of guesses! The word was {word}")

if __name__ == "__main__":
    play_game()