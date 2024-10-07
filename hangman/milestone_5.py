import random

word_list = ["Guava", "Apple", "Peach", "Blueberry", "Pear"]

class Hangman:
    
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def __check_guess__(self, guess): #method for checking if guessed letter is part of the word
        guess = guess.lower()
        if guess in set(self.word):
            print(f"Good Guess! {guess} is in the word.")
            for index,letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            print(f"With your letters revealed the word is {self.word_guessed}")
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
    
    def __ask_for_input__(self): #Asks the user for input, check if that input is a single letter then checks if that letter is in the word
        while True:
            guess = input("Input a single letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please enter a single alphabetical character.")
                self.__ask_for_input__()
            elif guess in set(self.list_of_guesses):
                print("You already tried that letter!")
                self.__ask_for_input__()
            else:
                self.__check_guess__(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list = word_list, num_lives = num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost.")
            break
        if game.num_letters > 0:
            game.__ask_for_input__()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game")
            break
            
play_game(word_list = word_list)