class Troglodyte:
    def __init__(self):
        self.backpack = []
        self.is_dead = False

    def insert_into_bacpack(self, item):
        self.backpack.append(item)