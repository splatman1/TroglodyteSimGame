class Person:
    """The Person class or character class is takes in properties from main to initialise characters
    as well as give the player dialogue and other items."""
    def __init__(self, name, message, item_wanted = False, item=None, item_name_wanted=None, tradable_item=None):
        self.character_message = message
        self.item = item
        self.name = name
        self.item_wanted = item_wanted
        self.item_name_wanted = item_name_wanted
        self.tradable_item = tradable_item




    def talk_to_character(self, location, backpack):
        print(self.character_message)
        if location.item is not None:
            items = []
            items.append(self.item)
            backpack.add(location, items)
        if self.item_wanted:
            backpack.sort()
            item_found = backpack.in_backpack(self.item_name_wanted.item)
            if item_found is None:
                print(f"A {self.item_name_wanted.item} is the only currency down here")
            if item_found == self.item_name_wanted.item:
                items = []
                items.append(self.tradable_item)
                backpack.add(location, items)
                print("A trade it is then")
                self.tradable_item = False
                self.item_name_wanted = False
                self.item_wanted = False

        else:
            return[]

    def remove_items(self):
        self.item = None









