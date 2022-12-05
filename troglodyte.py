import random
import sys
import time


class Troglodyte:
    """This is the Troglodyte class or the character the player will be playing as.
    It mainly holds dialogue options as well as the status of the troglodyte"""
    def __init__(self, backpack, player_viewable=True):
        self.is_alive = True
        self.starting_message = "what am I doing here?\n All I remember is being angry at something on r/PrequelMemes "\
                                "and waking up here.\n I need to hurry up and get out of here before someone has a " \
                                "cringe opinion on sonic 2006"

        self.choices = "\nWould you like to:\n " \
                                "1. Search Room\n" \
                                "2. Talk to character\n" \
                                "3. Look in backpack\n" \
                                "4. Collect Items\n" \
                                "5. Move Rooms\n"
        self.backpack = backpack
        self.player_viewable = player_viewable


    def ask_character_question(self, character):
        """This is called when the player wants to communicate with a player."""
        print(f"Hello There {character}")
        print("HI")


    def character_options(self):
        """This prints the players options which are listed above."""
        self.print_slow(self.choices)
        player_entry = input("What should I do? ")
        if player_entry.isnumeric():
            player_entry = int(player_entry)
            if player_entry < 6 and player_entry > 0:
                return player_entry

    def died(self):
        """This is only called by the dragon class to kill the player."""
        self.is_alive = False
        self.print_slow("Your Dead!!")
        print("DONT BE IMPATIENT, YOU MUST LOOK EXPLORE BEFORE\n YOU CAN BE FREE!")

    def print_slow(self, dialogue):
        """This is a print_slow function which makes the text printed look more like an
        old text based game."""
        dialogue = f"{dialogue}\n"
        for letter in dialogue:
            sys.stdout.write(letter)
            sys.stdout.flush()
            t = 0.01
            time.sleep(t)
