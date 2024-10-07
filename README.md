# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

##Table of contents
1. Project Description
1. Installation Instructions
1. Usage Instructions

###Project Description

This projects attempts to biuld a singel player version of the "Hangman" game.

### Installation Instructions

Clone the repo *link* and run the python file *milestone_5.py*

### Usage Instructions

Upon running *milestone_5.py* the program randomly chooses a word from a predetermined list. The user is then asked to input a string, the program then checks if the string is a single letter and if that letter is in the word. If succesful the program reveals this letter of the word, if not the user loses a life from a predetermined pool of lives. This process is repeated until the set of lives is exhausted or the entire word is revealed.