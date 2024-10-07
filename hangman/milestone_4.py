import random

word_list = ["Guava", "Apple", "Peach", "Blueberry", "Pear"]

class Hangman:
    
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in set(self.word):
            print(f"Good Guess! {guess} is in the word.")
            for index,letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
    
    def ask_for_input(self): #Asks the user for input, check if that input is a single letter then checks if that letter is in the word
        while True:
            guess = input("Input a single letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please enter a single alphabetical character.")
                self.ask_for_input()
            elif guess in set(self.list_of_guesses):
                print("You already tried that letter!")
                self.ask_for_input()
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        return guess

H1 = Hangman(word_list = word_list, num_lives = 5)
H1.ask_for_input()