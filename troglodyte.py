import random
import sys
import time


class Troglodyte:
    def __init__(self):
        self.is_alive = True
        self.starting_message = "what am I doing here?\n All I remember is being angry at something on r/PrequelMemes "\
                                "and waking up here.\n I need to hurry up and get out of here before someone has a " \
                                "cringe opinion on sonic 2006"
        self.dialogue_options = "Would you like to:\n " \
                                "1. Search Room" \
                                "2. Talk to character" \
                                "3. Look in backpack" \
                                "4. Collect Items"

    def died(self):
        self.is_alive = False
        print("Your Dead!!")

    def print_slow(self, dialogue):
        dialogue = f"{dialogue}\n"
        for letter in dialogue:
            sys.stdout.write(letter)
            sys.stdout.flush()
            t = 0.01
            time.sleep(t)
