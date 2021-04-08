import os

SCORES_FILE_NAME = "Scores.txt"
ERROR_MESSAGE = "Something went wrong.."
SCORE = 0

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')