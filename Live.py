from MemoryGame import Memorygmae
from GuessGame import Guessgmae
from Score import add_score
import Utils


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    memory_mame = Memorygmae()
    guess_name = Guessgmae()
    game_id = input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n")
    level = input("Please choose game difficulty from 1 to 5: ")
    if validate_input(int(game_id),int(level)) == False:
        return Utils.ERROR_MESSAGE
    else:
        win = memory_mame.play(level) if int(game_id) == 1 else  guess_name.play(level)
        print(str(win))
        if win == True:
            add_score(level)
        else:
            load_game()


def validate_input(game_id,level):
    return (game_id == 1 or game_id == 2) and (level <=5 or level >= 1)



