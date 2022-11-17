from items import Items
class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items):
        self._backpack = []
        if items is None:
            items = []
        if type(items) is not "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def remove(self, location):
        while True:
            item_number = input("Enter the item you wish to remove?")
            if item_number.isnumeric():
                item_number = int(item_number)
                if not self._backpack.index(item_number) == Items:
                    print("There is no item with that index")
                    break
                if self._backpack.index(item_number) == Items:
                    location.item1 = self._backpack.index(item_number)
                    self._backpack.remove(item_number)
            if not item_number.isnumeric():
                print("please enter a number")



    def sort(self):
        self._backpack.sort()

    def count(self):
        return self._backpack.count()

    def list(self):
        pass

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        return None