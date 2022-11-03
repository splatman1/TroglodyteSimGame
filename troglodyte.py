class Troglodyte:
    def __init__(self):
        self.backpack = []
        self.is_alive = True

    def insert_into_bacpack(self, item):
        self.backpack.append(item)

    def died(self):
        self.is_alive = False
        print("Your Dead!!")