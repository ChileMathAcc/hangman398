import random

word_list = ["Guava", "Apple", "Peach", "Blueberry", "Pear"] #List of possible words in Hangman
print(word_list)

word = random.choice(word_list).lower() #Pick out a random word from the list of possible words
print(word)

def ask_for_input(): #Asks the user for input, check if that input is a single letter then checks if that letter is in the word
    while True:
        guess = input("Input a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
    check_guess(guess)
    return guess
        
def check_guess(guess): #checks is the guessed letter is in the word
    guess = guess.lower()
    if guess in set(word):
        print(f"Good Guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")