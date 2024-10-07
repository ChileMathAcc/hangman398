import random

word_list = ["Guava", "Apple", "Peach", "Blueberry", "Pear"]
print(word_list)

def select_random_word(word_list):
    word = random.choice(word_list)
    return word

word = select_random_word(word_list)

print(word)

guess = input('Input a single letter: ')
if len(guess) == 1 and guess.isalpha():
    print('Good guess')
else:
    print('Oops! That is not a valid input.')
    
