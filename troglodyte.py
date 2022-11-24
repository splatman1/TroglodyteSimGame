import random
import sys
import time


class Troglodyte:
    def __init__(self, backpack):
        self.is_alive = True
        self.starting_message = "what am I doing here?\n All I remember is being angry at something on r/PrequelMemes "\
                                "and waking up here.\n I need to hurry up and get out of here before someone has a " \
                                "cringe opinion on sonic 2006"

        self.choices = "Would you like to:\n " \
                                "1. Search Room\n" \
                                "2. Talk to character\n" \
                                "3. Look in backpack\n" \
                                "4. Collect Items\n" \
                                "5. Move Rooms\n"
        self.backpack = backpack


    def ask_character_question(self, character):
        print(f"Hello There {character}")
        print("HI")


    def character_options(self):
        self.print_slow(self.choices)
        player_entry = input("What should I do? ")
        if player_entry.isnumeric():
            player_entry = int(player_entry)
            if player_entry < 6 and player_entry > 0:
                return player_entry

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
