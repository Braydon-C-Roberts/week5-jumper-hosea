import os
import graphics
import words

if os.name == "nt":
    CLS = "cls"
else: 
    CLS = "clear"

"""
Side Note: Encapsulate the current_word i.e. 
self.current_word = word_list(Random_word).
Create an array of words (string format) that can be randomly
selected for the current_word.
"""


class Director():
    def __init__(self) -> None:
        self.current_word = words.pick()
        self.number_of_tries = 4
        self.graphics = graphics.Graphics(self)


    def run(self):
        guessed = []
        lives = self.number_of_tries
        while True:
            # graphics.print_guess(self.current_word, guessed)
            # graphics.print_jumper(self.number_of_tries-lives)
            self.graphics.display()
            user_input = input("Pick a letter from A - Z: ")
            if user_input == "exit":
                os.system(CLS)
                print("Thanks for playing!")
                break

            if user_input in self.current_word:
                guessed.append(user_input)
            else:
                lives -= 1

            if self.check_victory(guessed):
                os.system(CLS)
                print("Congrats! You Win!\n\n\n")
                break

            elif lives == 0:
                os.system(CLS)
                # graphics.print_guess(self.current_word, guessed)
                # graphics.print_dead()
                self.graphics.display_dead()
                print("You Lose!\n\n\n")
                break
    
    def check_victory(self, guessed):
        characters = "" .join(guessed)
        if len(self.current_word.strip(characters)) == 0:
            return True
        return False