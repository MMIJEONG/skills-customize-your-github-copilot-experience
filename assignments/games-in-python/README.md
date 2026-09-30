# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice strings, loops, conditionals, random selection, and user input while tracking the game's progress.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word and prepare the game state that will be used to reveal letters and track incorrect guesses.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Initialize a collection of guessed letters and a maximum number of incorrect guesses.
- Display one placeholder for each letter in the secret word, revealing letters that have been guessed correctly.

### 🛠️ Implement Guessing and Game Results

#### Description
Run the game until the player guesses the word or runs out of allowed incorrect guesses. Give clear feedback after each guess and when the game ends.

#### Requirements
Completed program should:

- Repeatedly ask the player for a letter and update the displayed progress after each valid guess.
- Track incorrect guesses and reduce the remaining attempts only when a new incorrect letter is guessed.
- End the game when every letter in the secret word has been guessed or no attempts remain.
- Display a win message when the word is guessed and a loss message with the secret word when attempts run out.
