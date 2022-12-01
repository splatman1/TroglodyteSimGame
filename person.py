class Person:
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
            print(self.item.item)
            items = []
            items.append(self.item)
            backpack.add(location, items)
        if self.item_wanted:
            item_returned = backpack.in_backpack(location, self.item_name_wanted)
            if item_returned is None:
                print("You dont have what I need yet")
            if item_returned == self.item_name_wanted:
                print("A trade it is then")
                backpack.add(location, self.tradable_item)
                self.tradable_item = None


        else:
            pass

    def remove_items(self):
        self.item = None









