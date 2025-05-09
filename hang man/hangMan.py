import random
from Words import words  # Make sure this is a list of words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()

    lives = 6

    print("Welcome to Hangman!")
    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("Used letters:", ' '.join(sorted(used_letters)))
        
        # Show current word with guessed letters
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"Oops! '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("You already guessed that letter. Try another.")
        else:
            print("Invalid input. Please enter a letter.")

    if lives == 0:
        print(f"\nGame over! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

# Start the game
user_input = input("Press ENTER to start the game: ")
hangman()
