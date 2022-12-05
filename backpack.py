from items import Items
class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items=None):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    # def remove(self, location):
    #     while True:
    #         item_number = input("Enter the item you wish to remove?")
    #         if item_number.isnumeric():
    #             item_number = int(item_number)
    #             if not self._backpack.index(item_number) == Items:
    #                 print("There is no item with that index")
    #                 break
    #             if self._backpack.index(item_number) == Items:
    #                 location.item1 = self._backpack.index(item_number)
    #                 self._backpack.remove(item_number)
    #         if not item_number.isnumeric():
    #             print("please enter a number")
    def remove(self, item):
        """This removes items from the backpack by taking in the item it wishes to remove."""
        self.sort()
        self._backpack.remove(item.item)



    def get_key(self, item):
        return item.item
    def sort(self):
        """Lists have trouble adding instances to them so this assigns a key so it won't break"""
        self._backpack.sort(key=self.get_key)

    def count(self):
        pass

    def list(self):
        """The list function prints out all the items in the players backpack.
        If the player has nothing it will print a famous quote from charlie and the chocolate factory"""
        if len(self._backpack) == 0:
            print("You have nothing!, You lose!")
        print(" I'm a backpack loaded up with things and knickknacks too.\n"
              "Anything that you might need I've got inside for you.")
        for i in self._backpack:
            print(i.item)

    def add(self, location, items):
        """The add function takes in a list of items and adds them to the backpack"""
        items = items
        for i in items:
            if i is not None:
                print(f"Adding {i.item} to backpack")
                if i.is_collectable:
                    self._backpack.append(i)
                    location.remove_items()
                    self.sort()


    def in_backpack(self, target):
        """
        This function checks the players
        backpack for items and returns it if it is found.
        This is mainly used for keys and other item requirements.
        """
        self.sort()

        min_value = 0
        max_value = len(self._backpack)-1
        while min_value <= max_value:
            middle = (min_value + max_value)//2
            midpoint = self._backpack[middle].item
            if midpoint > target:
                max_value = middle - 1
            if midpoint < target:
                min_value = middle + 1
            else:
                return midpoint
        return None



