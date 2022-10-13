import os

if os.name == "nt":
    CLS = "cls"
else: 
    CLS = "clear"

class Director():
    def __init__(self) -> None:
        self.current_word = "python"
        pass


    def run(self):
        guessed = []
        lives = 4
        while True:
            user_input = input("Pick a letter from A - Z: ")
            if user_input == "exit":
                os.system(CLS)
                print("Thanks for playing!")
                break

            if user_input in self.current_word:
                guessed.append(user_input)
                print(guessed)

            else:
                print("No")
                lives -= 1

            if self.check_victory(guessed):
                os.system(CLS)
                print("Congrats! You Win!\n\n\n")
                break

            elif lives == 0:
                os.system(CLS)
                print("You Lose!\n\n\n")
                break
    
    def check_victory(self, guessed):
        characters = "" .join(guessed)
        if len(self.current_word.strip(characters)) == 0:
            return True
        return False