import random
from words import words
import string

def valid_words(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_words(words)
    word_letters =set(word)
    aphabets = set(string.ascii_uppercase)
    used_letters=set()
    lives = len(word) + 5
    while len(word_letters)>0 and lives>=0:
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ",' '.join(word_list))
        user_letter = input("Guess the letter: ").upper()
        print("----------------------------")
        if user_letter in aphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("Sorry ! You have already used that letter try again")
        else:
            print("Invalid character, Try again")
        print(f"Lives Left: {lives}")
        lives-=1
        print("you have used: ",' '.join(used_letters))
    lives_left = len(word) + 5 -lives
    if len(word_letters)==0:
        print(f"Congratulations you have guessed the words in {lives_left} Lives")
    else:
        print("YOU ARE DEAD !!!")
        
    
hangman()


    

