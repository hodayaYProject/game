import random

class Guessgmae:

    # Will get a number variable named difficulty,
    # Will return a random number between 1 to difficulty.
    def generate_number(self,difficulty):
        number_rundom = random.randrange(1,int(difficulty)) if difficulty != '1' else 1
        return number_rundom

    # Will get a number variable named difficulty,
    # Will ask the user to guess a number between 1 to difficulty and return the number the user guessed
    def get_guess_from_user(self,difficulty):
        guess = input(f"guess a number between 1 to {difficulty}: ")
        return guess

    # Will get 2 variables: number variable named difficulty number variable named ,
    # Will compare the secret generated number to the one prompted by the  get_guess_from_user.
    def compare_results(self,difficulty, secret_number):
        guess = self.get_guess_from_user(difficulty)
        return guess == secret_number

    #  Will get a number variable named difficulty,
    # Will return True / False if the user lost or won
    def play(self,difficulty):
        number = self.generate_number(difficulty)
        return self.compare_results(difficulty,str(number))
