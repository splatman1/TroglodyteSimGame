class Person:
    def __init__(self, name, message, item_wanted = None, item=None):
        self.character_message = message
        self.item = item
        self.name = name
        self.item_wanted = item_wanted

    def get_item_wanted(self, item):
        self.item_wanted = item

    def talk_to_character(self, location, backpack):
        print(self.character_message)
        if location.item is not None:
            print(self.item.item)
            backpack.add(location, self.item)
        else:
            pass

    def remove_items(self):
        self.item = None









