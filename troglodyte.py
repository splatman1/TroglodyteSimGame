import random
import sys
import time


class Troglodyte:
    def __init__(self, location):
        self.backpack = []
        self.is_alive = True
        self.location = location
        self.starting_message = "what am I doing here?"


    def insert_into_bacpack(self, item):
        self.backpack.append(item.item)

    def died(self):
        self.is_alive = False
        print("Your Dead!!")

    def print_slow(self, dialogue):
        for letter in dialogue:
            sys.stdout.write(letter)
            sys.stdout.flush()
            t = random.uniform(0.01,0.1)
            time.sleep(t)
