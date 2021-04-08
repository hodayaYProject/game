import Utils

# The function’s input is a variable called points
# The function will try to read the current score in the scores file, if it fails it will create a
# new one and will use it to save the current score.
# The function will print the user current score.
def add_score(point):
    file = open(Utils.SCORES_FILE_NAME,'rt')
    file_poits = file.read()
    poits = int(point) + int(file_poits)
    file_poits = file_poits.replace(file_poits,str(poits))
    file.close()
    file = open(Utils.SCORES_FILE_NAME, 'wt')
    file.write(file_poits)
    Utils.SCORE = poits
    file.close()
    print(f"The current points: {poits}")

