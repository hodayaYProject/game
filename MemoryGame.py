from random import randrange
import time
import Utils

class Memorygmae():


    # Will get a number variable named difficulty
    # Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
    # The list will be shown for 0.7 seconds (using Utils.py module).
    def generate_sequence(self,difficulty):
        randome_list = []
        for i in range(int(difficulty)):
            randome_list.append(randrange(1,101))
        print(randome_list)
        time.sleep(7)
        Utils.screen_cleaner()
        return randome_list


    # Will get a number variable named difficulty , the user type his number into a list
    # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
    def get_list_from_user(self,difficulty):
        print("After seeing the numbers enter the numbers you saw, each one separated with Enter: ")
        user_list = []
        for i in range(int(difficulty)):
            user_list.append(int(input()))
        return user_list

    # Will get 2 variables named list_a and list_b
    # The function will compare the two lists (list_a & list_b).
    # The function will return True / False if the lists equal or not.
    def is_list_equal(self, list_a, list_b):
        return  list_a == list_b

    # Will get a number variable named difficulty
    # Will call the functions above and play the game.
    # Will return True / False if the user lost or won (based on is_list_equal()).
    def play(self,difficulty):
        return self.is_list_equal(self.generate_sequence(difficulty),self.get_list_from_user(difficulty))


