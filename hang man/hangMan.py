import random
from words import words
 
 def get_valid_word(words):
 word= random.choice(words) # Randomly select a word from the list
    while '-' in word or ' ' in word: # Check if the word contains a hyphen or space
        word= random.choice(words) # If it does, select another word
    return word
# Return the word in uppercase
def hangman():
word= get_valid_word(words).upper() # Get a valid word and convert it to uppercase
word_letters= set(word) # Create a set of letters in the word
alphabet= set(string.ascii_uppercase) # Create a set of uppercase letters
used_letters= set() # Create a set to keep track of used letters
 

 user
